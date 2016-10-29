# -*- coding: utf-8 -*-

DEFAULT_PORT = 5000
ADDITIVE_FOR_UID = 1000

try:
    from os import getuid

except ImportError:
    def getuid():
        return DEFAULT_PORT - ADDITIVE_FOR_UID

from time import sleep

from celery import Celery
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import urllib2
import re
from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__)
app.config.update({
    'CELERY_BACKEND': 'mongodb://localhost/celery',
    'CELERY_BROKER_URL': 'amqp://guest:guest@localhost:5672//'
})


def make_celery(app):
    celery = Celery('backend.main', backend=app.config['CELERY_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


celery = make_celery(app)


@celery.task
def long_running_job(click_count):
    sleep(5)
    return click_count ** 3


@app.route('/fuckthis', methods=["POST"])
def kek():
    print request.form
    imd = ImmutableMultiDict(request.form)
    imd = dict(imd)
    print imd['text'][0]
  #  print jsonify(data=request.form)
    try:
        a = urllib2.urlopen(imd['text'][0])
        b = a.read()
        le = len(b)
    except TypeError:
        le = "Unable to load your page"
    except ValueError:
        le = "Unable to load your page"
    except URLError:
        le = "Unable to load your page"
    try:
        words = count_words(b)
    except UnboundLocalError:
        words = 0
    return str(str(le) + " chars, " + str(words) + " words in visible text")
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match(u'<!--.*-->', unicode(element)):
        return False
    return True
def count_words(page):
    html = page
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(visible, texts)
    big_string = ''
    for i in visible_texts:
        big_string += ' '
        big_string += i
    print big_string
    splitted = big_string.split()
    print(len(splitted))
    return(len(splitted))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    click_count = int(request.args.get('cc', 0))
    task_id = long_running_job.delay(click_count)

    return jsonify({
        'count': click_count,
        'squared': click_count ** 2,
        'task_id': str(task_id)
    })


@app.route('/result/<task_id>')
def result(task_id):
    async_result = celery.AsyncResult(task_id)

    return jsonify({
        'ready': async_result.ready(),
        'status': async_result.status,
        'result': async_result.result,
        'task_id': str(async_result.task_id)
    })
@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = text.upper()
    #return str(count_words(processed_text))
    return jsonify({'words_no': str(count_words(processed_text))})
''''
def count_words(address):
    try:
        a = urllib2.urlopen(address)
        b = a.read()
        le = len(b)
    except TypeError:
        le = "Unable to load your page"
    except ValueError:
        le = "Unable to load your page"
    return le
'''
if __name__ == '__main__':
    app.run(port=getuid() + ADDITIVE_FOR_UID, debug=True)

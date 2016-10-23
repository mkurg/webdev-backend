// DOM is ready
$(document).ready(function () {
  var click_count = 0;

  // Bind click event
  $('.pushme').click(function () {
    click_count += 1;

    // AJAX request
    $.get('/data?cc=' + click_count, function (data) {
      var row_html = 
          '<tr><td>' + data.count + '</td>' +
          '<td>' + data.squared + '</td></tr>';

      // Append our row
      $('.ourtable > tbody').append(row_html);
    });

    return false;
  });
});

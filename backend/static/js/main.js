// DOM is ready
// $(document).ready(function () {
//   // Polling function
//   var polling = function (task_id) {
//     $.get('/result/' + task_id, function (data) {
//       if (data.ready) {
//         $('.modal-body').html('<p>From task ' + data.task_id +
//                               ' we got: ' + data.result);
//         $('.modal').modal('show');
//       } else {
//         setTimeout(function () {
//           polling(task_id);
//         }, 1000);
//       }
//     });
//   };

//   var click_count = 0;
  //$("#addressForm").submit(function (e) {
    //alert('hello')
    //sendAddressForm();
    //e.preventDefault();
    // return false;
 // })

 // $('form#addressForm').submit(function (event) {
   // var address = $('#eIE').val();

  //  click_count += ;

    // AJAX
  //  $.get('/data?cc=' + click_count + '&address' + address, function  (data))
  //   var row_html = '<tr><td>' + data.count + '</td>' +
  //         '<td>' + data.squared + '</td>' + '<td>' + data.email + '</td></tr>';
  //          // Append our row
  //     $('.ourtable > tbody').append(row_html);

    

  //     return false;
  // })

  $("#buttonSubmit").click(function () {
    url = $("#eIE").val()
    $.post('/fuckthis', {text: url}).done(function       (data){
          //alert(JSON.stringify(data));
          var row_html = '<tr><td>' + url + '<td>' + JSON.stringify(data) + '</td></tr>'
      
      $('.ourtable > tbody').append(row_html);
     }); 
  })
  

//   // Bind click event
//   $('.pushme').click(function () {
//     click_count += 1;

//     // AJAX request
//     $.get('/data?cc=' + click_count, function (my_form_post) {
//       var row_html = 
//           '<tr><td>' + my_form_post.words_no + '</td>' +
//           '<td>' + my_form_post.words_no + '</td></tr>';

//       // Append our row
//       $('.ourtable > tbody').append(row_html);

//       // Run polling for task
//       polling(data.task_id);
//     });

//     return false;
//   });
// });

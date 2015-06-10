$(function() {
  var $form = $('.typograph-form');
  var $input = $('.typograph-form_input');
  var $output = $('.typograph-form_output');

  $form.submit(function(e) {
    var input = $input.val();
    $.post('/process', { text: input }).then(function(output) {
      $output.val(output);
    });
    e.preventDefault();
  });

  $input.keyup(_.throttle(function() {
    $form.submit();
  }, 600));
});

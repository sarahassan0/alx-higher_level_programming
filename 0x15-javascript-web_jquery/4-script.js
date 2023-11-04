$(document).ready(function () {
    $('DIV#toggle_header').on('click', function () {
      if (header.hasClass('red')) {
        header.removeClass('red').addClass('green')
      } else if ($('header').attr('class') === 'green') {
        header.removeClass('green').addClass('red');
      }
    });
  });

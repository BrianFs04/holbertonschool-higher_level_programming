document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      convert();
    }
  });
  $('INPUT#btn_translate').click(function () {
    convert();
  });
  function convert () {
    const lang = $('INPUT#language_code').val();
    const link = 'https://fourtonfish.com/hellosalut/?lang=';
    $.ajax({
      type: 'GET',
      url: `${link}${lang}`,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }
});

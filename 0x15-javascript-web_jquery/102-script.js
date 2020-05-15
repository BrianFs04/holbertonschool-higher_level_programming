document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const link = 'https://fourtonfish.com/hellosalut/?lang=';
    $.ajax({
      type: 'GET',
      url: `${link}${lang}`,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    fetch('https://www.fourtonfish.com/hellosalut/?lang=' + lang)
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonData) {
        $('div#hello').text(jsonData.hello);
      });
  });
  $('input#language_code').keypress(function (e) {
    const key = e.which;
    if (key == 13) {
      $('input#btn_translate').click();
      return false;
    }
  });
});

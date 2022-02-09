$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (salut) {
      $('div#hello').text(salut.hello);
    }
  });
});

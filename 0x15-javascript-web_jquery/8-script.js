$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function (index, movie) {
        $('ul#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});

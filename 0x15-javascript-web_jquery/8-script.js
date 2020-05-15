$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, d) {
        $('UL#list_movies').append('<li>' + d.title + '</li>');
      });
    }
  });
});

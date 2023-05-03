$(function() {
  const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
  
  $.get(url, function (data) {
    const movies = data.results;
    const list = $("<ul></ul>");
    $.each(movies, function (index, movie) {
      const item = $("<li></li>");
      item.text(movie.title);
      item.appendTo(list);
    });
    list.appendTo("ul#list_movies");
  });
});  

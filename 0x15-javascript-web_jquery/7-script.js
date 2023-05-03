#!/usr/bin/node

$(function() {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function (data, textStatus)
  {
    const name = JSON.stringify(data);
    $('<p>' + name + '</p>').appendTo('DIV#character');
  });
});

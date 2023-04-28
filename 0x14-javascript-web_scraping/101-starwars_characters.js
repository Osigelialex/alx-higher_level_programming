#!/usr/bin/node

const request = require('request');
const BASE_URL = "https://swapi.dev/api/";
const FILMS_ENDPOINT = "films/";
const CHARACTERS_ENDPOINT = "people/";
const movie_id = process.argv[2];

const film_url = BASE_URL + FILMS_ENDPOINT + movie_id;

request(film_url, function(error, response, body) {
  if (!error && response.statusCode == 200) {
    const film_data = JSON.parse(body);

    const characters = film_data.characters;

    characters.forEach(function(character_url) {
      request(character_url, function(error, response, body) {
        if (!error && response.statusCode == 200) {
          const character_data = JSON.parse(body);
          console.log(character_data.name);
        } else {
          console.error(error);
        }
      });
    });
  } else {
    console.error(error);
  }
});


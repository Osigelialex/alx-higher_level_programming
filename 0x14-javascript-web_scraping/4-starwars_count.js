#!/usr/bin/node

const request = require('request');

const API = process.argv[2];
const characterId = '18';

request(API, { json: true }, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    const movies = data.results.filter(movie => {
      return movie.characters.find(c => c.endsWith(`/${characterId}/`));
    });
    console.log(`${movies.length}`);
  }
});

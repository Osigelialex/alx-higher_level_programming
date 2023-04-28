#!/usr/bin/node

const request = require('request');

const API = process.argv[2];

const options = {
  url: API,
  json: true
};

request(options, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const completed = body.filter(obj => obj.completed === true);
    const number = {};

    for (let i = 1; i <= 10; i++) {
      const counter = completed.reduce((count, value) =>
        (value.userId === i ? count + 1 : count), 0);
      number[i] = counter;
    }

    console.log(number);
  }
});

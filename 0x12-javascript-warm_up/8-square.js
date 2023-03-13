#!/usr/bin/node

const process = require('process');
const value = process.argv[2];
let square = '';

if (isNaN(value)) {
  console.log('Missing Size');
}
if (value > 0) {
  for (let i = 0; i < value; i++) {
    for (let j = 0; j < value; j++) {
      square += 'x';
    }
    if (i !== value - 1) {
      square += '\n';
    }
  }
  console.log(square);
}

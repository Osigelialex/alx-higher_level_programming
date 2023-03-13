#!/usr/bin/node

const process = require('process');
const value = process.argv[2];

if (isNaN(value)) {
  console.log('Missing Size');
}
if (value > 0) {
  for (let i = 0; i < value; i++) {
    console.log('X'.repeat(value));
  }
}

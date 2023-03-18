#!/usr/bin/node
const array = require('./100-data').list;

console.log(array);
let idx = 0;
const map1 = array.map(x => x * idx++);
console.log(map1);

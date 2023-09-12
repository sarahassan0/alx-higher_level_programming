#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((item, indx) => item * indx);

console.log(list);
console.log(newList);

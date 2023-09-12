#!/usr/bin/node
const list = require('./100-data').list;

const new_list = list.map((item, indx) => item * indx);

console.log(list);
console.log(new_list);

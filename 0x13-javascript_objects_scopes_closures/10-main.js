#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

myConverter = converter(16);

console.log(myConverter(2));
// console.log(converter(16)(2)); also valid to call function that returns function
console.log(myConverter(12));
console.log(myConverter(89));

#!/usr/bin/node

const num = parseInt(process.argv[2]);
console.log(`My number: ${isNaN(num) ? 'Not a number' : num}`);

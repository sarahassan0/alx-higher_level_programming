#!/usr/bin/node

function factorial (num) {
  return((!num || num === 1) ? 1 : num * factorial(num - 1));
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));

#!/usr/bin/node

function factorial (num) {
  if (!num || num === 1) return 1;
  const fact = num * factorial(num - 1);
  return fact;
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));

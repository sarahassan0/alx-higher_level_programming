#!/usr/bin/node

let num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing number of occurrences');
} else if (num > 0) {
  while (num--) {
    console.log('C is fun');
  }
}

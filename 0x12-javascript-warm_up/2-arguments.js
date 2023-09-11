#!/usr/bin/node

const arg = process.argv.length;
if (arg === 2) {
  console.log('No argument');
} else if (arg === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}

#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing size');
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) process.stdout.write('X');
    console.log();
  }
}

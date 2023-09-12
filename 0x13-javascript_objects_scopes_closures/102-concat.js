#!/usr/bin/node
const fs = require('fs');

const str1 = fs.readFileSync(process.argv[2]);
const str2 = fs.readFileSync(process.argv[3]);
fs.writeFileSync(process.argv[4], str1 + str2);

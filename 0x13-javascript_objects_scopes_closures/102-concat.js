#!/usr/bin/node
const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2]);
const sArg = fs.readFileSync(process.argv[3]);
fs.writeFileSync(process.argv[4], fArg + sArg);

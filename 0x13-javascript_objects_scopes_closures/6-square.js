#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    c = (!c) ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;

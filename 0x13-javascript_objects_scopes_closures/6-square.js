#!/usr/bin/node

const Sq = require('./5-square');
module.exports = class Square extends Sq {
  charPrint (c) {
    let p = '';
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        p += c;
      }
      if (i === this.height - 1) {
        break;
      }
      p += '\n';
    }
    console.log(p);
  }
};

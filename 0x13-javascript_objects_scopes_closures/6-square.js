#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let p = '';
    if (!c) {
      Rectangle.prototype.print.call(this);
      return;
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

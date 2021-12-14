#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0) {
      return;
    }
    if (!Number.isInteger(h) || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let p = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        p += 'X';
      }
      if (i === this.height - 1) {
        break;
      }
      p += '\n';
    }
    console.log(p);
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

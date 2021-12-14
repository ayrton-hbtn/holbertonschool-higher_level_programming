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
};

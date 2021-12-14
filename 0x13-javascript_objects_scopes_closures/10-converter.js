#!/usr/bin/node

exports.converter = function (base) {
  function getNum (n) {
    return n.toString(base);
  }
  return getNum;
};

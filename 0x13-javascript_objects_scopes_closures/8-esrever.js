#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  let l = list.length;
  for (l = l - 1; list[l]; l--) {
    rev.push(list[l]);
  }
  return rev;
};

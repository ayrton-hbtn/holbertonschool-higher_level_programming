#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (!list) {
    return;
  } else {
    for (let i = 0; list[i]; i++) {
      if (searchElement === list[i]) {
        count++;
      }
    }
  }
  return (count);
};

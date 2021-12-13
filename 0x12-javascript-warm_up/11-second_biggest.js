#!/usr/bin/node

const arr = process.argv;
let max = -Infinity; let res = -Infinity;
if (!arr[2] || arr.length < 4) {
  console.log(0);
} else {
  for (let i = 2; arr[i]; i++) {
    const tmp = parseInt(arr[i]);
    if (max < tmp) {
      [res, max] = [max, tmp];
    } else if (res < tmp && tmp < max) {
      res = tmp;
    }
  }
  console.log(res);
}

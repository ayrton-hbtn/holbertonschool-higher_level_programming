#!/usr/bin/node

const argv = process.argv;
if (!parseInt(argv[2])) {
  console.log(1);
}

function factorial (a) {
  if (a <= 1) {
    return 1;
  }
  return (a * factorial(a - 1));
}

console.log(factorial(argv[2]));

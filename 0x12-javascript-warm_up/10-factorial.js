#!/usr/bin/node

function factorial (a) {
  if (a <= 1) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

const argv = process.argv;

if (!argv[2] || !parseInt(argv[2])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(argv[2])));
}

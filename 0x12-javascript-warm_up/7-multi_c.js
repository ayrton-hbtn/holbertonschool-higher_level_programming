#!/usr/bin/node

const argv = process.argv;
if (!argv[2] || !parseInt(argv[2])) {
  console.log('Missing number of occurrences');
} else if (parseInt(argv[2]) >= 0) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}

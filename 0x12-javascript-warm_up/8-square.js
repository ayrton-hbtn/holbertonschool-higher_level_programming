#!/usr/bin/node

const argv = process.argv;
let str = '';
if (!argv[2] || !parseInt(argv[2])) {
  console.log('Missing size');
} else if (parseInt(argv[2]) >= 0) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    str = '';
    for (let i = 0; i < parseInt(argv[2]); i++) {
      str += 'X';
    }
    console.log(str);
  }
}

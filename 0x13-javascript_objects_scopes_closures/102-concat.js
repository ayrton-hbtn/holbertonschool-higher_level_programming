#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
try {
  let data = fs.readFileSync(argv[2], 'utf8');
  data += fs.readFileSync(argv[3], 'utf8');
  fs.writeFileSync(argv[4], data);
} catch (err) {
  console.error(err);
}

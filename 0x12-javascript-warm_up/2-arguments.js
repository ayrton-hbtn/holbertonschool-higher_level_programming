#!/usr/bin/node

const { argv } = require('process');

if (argv.slice(2).length < 1) {
  console.log('No Argument');
} else if (argv.slice(2).length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

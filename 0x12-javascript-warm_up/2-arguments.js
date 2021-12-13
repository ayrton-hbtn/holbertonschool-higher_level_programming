#!/usr/bin/node

const args = process.argv.length;

if (args < 3) {
  console.log('No Argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

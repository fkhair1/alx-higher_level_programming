#!/usr/bin/node
const args = process.argv;
if (args.length > 2) {
  for (const i = 0; i < args[2]; i++) {
  console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

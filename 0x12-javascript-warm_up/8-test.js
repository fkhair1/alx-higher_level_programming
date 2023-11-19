#!/usr/bin/node
const args = process.argv;
if (args.length > 2) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    for (let j = 0; j < parseInt(args[2]); j++) {
    console.log('X');
  }
  }
} else {
  console.log('Missing size');
}

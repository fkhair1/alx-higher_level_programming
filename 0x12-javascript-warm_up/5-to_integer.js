#!/usr/bin/node
const args = process.argv;
if (ParsInt(args[2])){
  console.log('My number: ' + ParsInt(args[2]));
} else{
  console.log('Not a number');
}

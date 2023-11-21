#!/usr/bin/node
function add(a, b) {
  return a+b;
}
const args = process.argv;
if (parseInt(args[2]) && parseInt(args[3])) {
  console.log(add((parseInt(args[2])), (parseInt(args[3]))));
}

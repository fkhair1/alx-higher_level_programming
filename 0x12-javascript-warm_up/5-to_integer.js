#!/usr/bin/node
const args = process.argv;
if (ParseInt(args[2])){
  console.log('My number: ' + ParseInt(args[2]));
} else{
  console.log('Not a number');
}

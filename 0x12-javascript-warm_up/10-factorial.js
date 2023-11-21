#!/usr/bin/node
const args = process.argv;
function factorial (a) {
 if (parseInt(a)) {
  let n = 1;
  for (let i = 0; i <= parseInt(a); i++) {
    console.log(n = n * i);
    } 
 } else {
    console.log(1);
  }
}
factorial (args[2]);

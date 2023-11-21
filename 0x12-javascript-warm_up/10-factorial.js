#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  let n = 1;
  if (parseInt(a)) {
    for (let i = 1; i <= parseInt(a); i++) {
      n = n * i;
    }
  }
   console.log(n);
}
factorial (args[2]);

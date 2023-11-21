#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  if (parseInt(a)) {
    for (let i = 0; i <= parseInt(a); i++) {
      console.log(a = a * i);
    }
  } else {
    console.log(1);
  }
}

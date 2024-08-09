let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const arr = input.map(Number);
let idx = -1, num = -1;

for(let i=0; i<9; i++) {
  if (num<arr[i]) {
    idx = i;
    num = arr[i];
  }
}

console.log(`${num}\n${idx+1}`);
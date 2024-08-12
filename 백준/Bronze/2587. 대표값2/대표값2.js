let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let arr = [];
for(let i=0; i<5;i++) {
  arr.push(Number(input[i]));
}

let sum=0;
for (a of arr) {
  sum += a;
}

console.log(parseInt(sum/5));

arr.sort();
console.log(arr[2]);
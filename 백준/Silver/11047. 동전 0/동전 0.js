let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, k] = input[0].split(" ").map(Number);
let arr = []

for (let i=1; i<n+1; i++) {
  arr.push(Number(input[i]));
}

let idx = n-1;
let answer = 0;

while (k != 0) {
  if (k/arr[idx] >= 1) {
    answer += parseInt(k/arr[idx]);
  } 
  k %= arr[idx];
  idx--;
}

console.log(answer);
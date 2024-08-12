let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let arr = input[1].split(" ").map(Number).sort((a,b) => a-b);

let answer = 0;
let cumulative = 0;
for (let i=0; i<n; i++) {
  cumulative += arr[i];
  answer += cumulative;
}

console.log(answer);

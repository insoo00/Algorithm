let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n")

let a = Number(input[0]);
let b = input[1];

answer = "";

for (let i = b.length - 1; i > -1; i--) {
  answer += a * Number(b[i]) + "\n";
}

answer += a * Number(b);

console.log(answer);

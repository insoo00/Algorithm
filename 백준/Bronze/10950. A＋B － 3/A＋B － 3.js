let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const T = Number(input[0]);

for (let i=1; i<=T; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  console.log(a+b);
}
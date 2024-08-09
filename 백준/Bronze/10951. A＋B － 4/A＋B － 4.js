let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let i = 0;
while(input[i]) {
  const [a, b] = input[i].split(" ").map(Number);
  console.log(a+b);
  i++;
}
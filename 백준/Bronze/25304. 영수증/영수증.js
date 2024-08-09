let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const total = Number(input[0]);
const n = Number(input[1]);

let calc = 0;
for (let i=2; i<n+2; i++) {
  const [price, quantity] = input[i].split(" ").map(Number);
  calc += price*quantity;
}

answer = "No"
if (total == calc) {
  answer = "Yes";
} 

console.log(answer);
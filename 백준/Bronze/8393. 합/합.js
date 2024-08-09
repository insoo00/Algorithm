let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString();
let input = fs.readFileSync("/dev/stdin").toString();

const n = Number(input);

let answer = 0
for(let i=1; i<=n; i++) {
  answer += i;
}

console.log(answer);
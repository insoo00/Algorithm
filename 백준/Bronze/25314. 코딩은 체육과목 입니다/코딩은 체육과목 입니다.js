let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString();
let input = fs.readFileSync("/dev/stdin").toString();

const n = Number(input);
let answer = "";

for (let i=0; i<(n/4); i++) {
  answer += "long ";
}

console.log(answer + "int")

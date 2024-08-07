let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim();
let input = fs.readFileSync("/dev/stdin").toString().trim();

let year = Number(input);
let answer = 0;

if (year % 4 == 0) {
  if ((year % 100 != 0) || (year % 400 == 0)) {
    answer = 1;
  }
}

console.log(answer)
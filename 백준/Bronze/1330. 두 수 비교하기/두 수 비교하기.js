let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split(" ");
let input = fs.readFileSync("/dev/stdin").toString().split(" ")

let a = Number(input[0]);
let b = Number(input[1]);

let answer = "";

if (a > b) {
  answer = ">";
} else if (a < b) {
  answer = "<";
} else {
  answer = "==";
}

console.log(answer);

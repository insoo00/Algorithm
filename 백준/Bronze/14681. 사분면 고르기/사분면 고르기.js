let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs.readFileSync(0, 'utf-8').trim().split('\n');


let x = Number(input[0]);
let y = Number(input[1]);

let answer = 0;

if (x > 0 && y > 0) {
  answer = 1;
} else if (x > 0 && y < 0) {
  answer = 4;
} else if (x < 0 && y > 0) {
  answer = 2;
} else {
  answer = 3;
}

console.log(answer);

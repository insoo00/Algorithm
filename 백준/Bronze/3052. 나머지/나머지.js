let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let arr = Array.from({ length: 42 }, () => 0);

for (let i = 0; i < 10; i++) {
  const num = Number(input[i]);
  arr[num%42] = 1;
}

let answer = 0;
for (let i=0; i<42; i++) {
  if (arr[i] == 1) {
    answer += 1
  }
}

console.log(answer)

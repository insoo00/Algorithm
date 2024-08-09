let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let arr = Array.from({length: 31}, () => -1);

for(let i=0; i<28; i++) {
  const num = Number(input[i]);
  arr[num] = 1;
}

let answer = "";
for(let i=1; i<31; i++) {
  if (arr[i] == -1) {
    answer += i + "\n";
  }
}

console.log(answer);

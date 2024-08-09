let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString();
let input = fs.readFileSync("/dev/stdin").toString();

const n = Number(input);


for (let i=0; i<n; i++) {
  let answer = "";
  for (let j=0; j<=i; j++) {
    answer += "*";
  }
  console.log(answer);
}

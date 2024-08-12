let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("-");

let answer = 0;
for(let i=0; i<input.length;i++) {
  let cur = input[i].split("+").map(Number).reduce((a,b) => a+b);
  if (i==0) answer += cur;
  else answer -= cur;
}

console.log(answer);


let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let arr = [];
for (let i=1; i<n+1; i++) {
  arr.push(input[i].split(" ").map(Number));
}

//끝나는 시간 -> 시작하는 시간 순으로 정렬
arr.sort((a, b) => {
  if(a[1] == b[1]) return a[0] - b[0];
  else return a[1]-b[1];
});

let answer = 0;
let cur =0;

for(let i=0; i<arr.length;i++) {
  if (cur <= arr[i][0]) {
    cur = arr[i][1];
    answer += 1;
  }
}

console.log(answer);
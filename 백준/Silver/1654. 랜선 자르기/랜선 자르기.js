let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, k] = input[0].split(" ").map(Number);
let arr = [];
for (let i=1; i<n+1; i++) {
  arr.push(Number(input[i]));
}

arr.sort((a,b) => a-b);

let left = 1;
let right = arr[n-1];

let answer = 0;
while (left <= right) {
  let mid = parseInt((left+right)/2);
  // console.log(left, right, mid);

  let cnt = 0;
  for (a of arr) {
    cnt += parseInt(a/mid);
  }

  if (cnt >= k) {
    answer = mid;
    left = mid+1;
  } else {
    right = mid-1;
  }
  // console.log(left, right, mid, cnt);
}

console.log(answer);
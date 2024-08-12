let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let arr = [];

for (let i=1; i<n+1; i++) {
  const current = input[i].split(" ").map(Number);
  arr.push(current);
  
}

arr.sort((a, b) => {
  if (a[0] != b[0]) {
    return a[0] - b[0];
  } else {
    return a[1] - b[1];
  }
});

for (let i=0; i<n; i++) {
  console.log(arr[i][0] + " " + arr[i][1]);
}
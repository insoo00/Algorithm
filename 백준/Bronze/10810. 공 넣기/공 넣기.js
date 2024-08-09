let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, m] = input[0].split(" ").map(Number);
let arr = Array.from({length: n+1}, () => 0);

for (let p=1; p<m+1; p++) {
  const [i, j, k] = input[p].split(" ").map(Number);
  for (let q=i; q<j+1; q++) {
    arr[q] = k;
  }
}

arr.splice(0, 1);
console.log(arr.join(" "));
let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, m] = input[0].split(" ").map(Number);
let arr = Array.from({length: n+1}, (_, i) => i)

for (let i=1; i<m+1; i++) {
  const [left, right] = input[i].split(" ").map(Number);
  [arr[left], arr[right]] = [arr[right], arr[left]]
}

arr.splice(0, 1);
console.log(arr.join(" "));
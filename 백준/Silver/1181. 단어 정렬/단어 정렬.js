let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let set = new Set();
for (let i=1; i<n+1; i++) {
  set.add(input[i]);
}

let arr = Array.from(set);
arr.sort((a, b) => {
  if (a.length != b.length) return a.length-b.length;
  else return a > b ? 1 : (a < b ? -1 : 0);
});

console.log(arr.join("\n"));

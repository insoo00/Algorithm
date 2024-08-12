let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, k] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number).sort((a,b) => a-b);

console.log(arr[n-k]);


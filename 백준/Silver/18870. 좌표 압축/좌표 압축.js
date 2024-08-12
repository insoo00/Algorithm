let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

let set = new Set(arr);
let setToArray = Array.from(set).sort((a, b) => a-b);

let dict = {};
for (let i=0; i<setToArray.length; i++) {
  dict[setToArray[i]] = i;
}

let answer ="";
for (let i=0; i<arr.length; i++) {
  answer += dict[arr[i]] + " ";
}

console.log(answer);
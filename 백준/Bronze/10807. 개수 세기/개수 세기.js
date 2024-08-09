let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const num = Number(input[2]);


let findArr = arr.filter(item => {
  return num == item;
})

console.log(findArr.length);
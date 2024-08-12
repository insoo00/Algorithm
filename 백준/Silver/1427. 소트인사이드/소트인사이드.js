let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim();
let input = fs.readFileSync("/dev/stdin").toString().trim();

let arr = [];
for (let i=0; i<input.length; i++) {
  arr.push(Number(input[i]));
}

arr.sort((a,b) => b-a);

console.log(arr.join(""))

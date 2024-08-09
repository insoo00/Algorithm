let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [N, X] = input[0].split(" ").map(Number);
const nums = input[1].split(" ").map(Number);

const answer = nums.filter(num => {
  return X > num;
})

console.log(answer.join(" "));
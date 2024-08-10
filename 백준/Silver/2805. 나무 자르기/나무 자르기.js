let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const heights = input[1].split(" ").map(Number).sort((a, b) => a-b);

let start = 1;
let end = heights[n-1];

let answer = 0;
while (start<=end) {
  let mid = parseInt((start+end)/2);
  let calcHeight = 0;

  for (height of heights) {
    calcHeight += Math.max(height-mid, 0);
  }
    
  if (calcHeight >= m) {
    answer = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(answer);
function binaySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;
  let answer = 0;

  while (left <= right) {
    let mid = parseInt((left + right) / 2);
    // console.log(left, right, mid)

    if (target < arr[mid]) {
      right = mid-1;
    } else if (target > arr[mid]) {
      left = mid +1;
    } else {
      answer = 1;
      break
    }
  }
  return answer;
}

let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let nArr = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

// console.log(nArr);

const m = Number(input[2]);
let mArr = input[3].split(" ").map(Number);

let answer = "";
for (let i = 0; i < m; i++) {
  answer += binaySearch(nArr, mArr[i]) + "\n"
}
console.log(answer);
function dfs(depth, calc) {
  if (depth == n) {
    minValue = Math.min(minValue, calc);
    maxValue = Math.max(maxValue, calc);
    return;
  }
  if (add > 0) {
    add--;
    dfs(depth+1, calc+arr[depth]);
    add++;
  } 
  if (sub > 0) { 
    sub--;
    dfs(depth+1, calc-arr[depth]);
    sub++;
  }
  if (mul > 0) {
    mul--;
    dfs(depth+1, calc*arr[depth]);
    mul++;
  }
  if (div >0) {
    div--;
    dfs(depth+1, parseInt(calc/arr[depth]));
    div++;
  }
  
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
let [add, sub, mul, div] = input[2].split(" ").map(Number);

let minValue = Number.POSITIVE_INFINITY;
let maxValue = Number.NEGATIVE_INFINITY;

dfs(1, arr[0]);

console.log(maxValue + "\n" + minValue);
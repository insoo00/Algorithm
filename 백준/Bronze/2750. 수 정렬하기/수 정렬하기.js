let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0])
let arr = []

for (let i=1; i<n+1; i++) {
  arr.push(Number(input[i]))
}

selectionSort(arr);
console.log(arr.join("\n"));

function selectionSort(arr) {
  for (let i=0; i<arr.length; i++) {
    let minIndex = i;
    for (let j=i+1; j<arr.length; j++) {
      if(arr[minIndex]>arr[j]) {
        minIndex = j;
      }
    }
    [arr[minIndex], arr[i]] = [arr[i], arr[minIndex]]
  }
}
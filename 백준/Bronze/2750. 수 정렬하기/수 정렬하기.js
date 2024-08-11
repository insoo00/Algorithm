function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let minIndex = i;
    for (let j = i; j < arr.length; j++) {
      if (arr[minIndex] > arr[j]) {
        minIndex = j;
      }
    }
    [arr[minIndex], arr[i]] = [arr[i], arr[minIndex]];
  }
}

function bubbleSort(arr) {
  for (let i=arr.length-1; i>0; i--) {
    for (let j=0; j<i; j++) {
      if (arr[j] > arr[j+1]) {
        [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
      }
    }
  }
}

function insertionSort(arr) {
  for (let i=1; i<arr.length; i++) {
    for (let j=i; j>0; j--) {
      if (arr[j-1] > arr[j]) {
        [arr[j-1], arr[j]] = [arr[j], arr[j-1]];
      } else {
        break;
      }
    }
  }
}

let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let nums = [];
for (let i = 1; i < n+1; i++) {
  nums.push(Number(input[i]));
}

insertionSort(nums);
console.log(nums.join("\n"));

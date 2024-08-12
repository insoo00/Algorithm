function merge(arr, left, mid, right) {
  let i = left;  //왼쪽 배열 인덱스
  let j = mid+1; //오른쪽 배열 인덱스
  let k = left;  //병합 배열 인덱스
  while (i<=mid && j<=right) {
    if (arr[i] <= arr[j]) sorted[k++] = arr[i++];
    else sorted[k++] = arr[j++];
  }
  if (i > mid) {
    while (j <= right) sorted[k++] = arr[j++];
  } else {
    while (i <= mid) sorted[k++] = arr[i++];
  }

  for (let x=left; x<=right; x++) arr[x] = sorted[x]
}

function mergeSort(arr, left, right) {
  if (left < right) {
    let mid = parseInt((left+right)/2);
    mergeSort(arr, left, mid);
    mergeSort(arr, mid+1, right);
    merge(arr, left, mid, right);
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
let sorted = Array.from({length: n}, () => -1)

mergeSort(nums, 0, n-1);
let answer = "";
for (num of nums) {
  answer += num + "\n";
}

console.log(answer)
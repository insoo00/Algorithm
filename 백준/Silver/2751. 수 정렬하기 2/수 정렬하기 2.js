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

function quickSort(arr, left, right) {
    if (left >= right) {
        return;
    }
    // [0, 원소 개수)에서 랜덤 값으로 pivot 지정
    let pivot = Math.floor(Math.random() * (right - left + 1)); 
    pivot += left;
    [arr[pivot], arr[left]] = [arr[left], arr[pivot]];
    pivot = left;
    let i = left + 1;
    let j = right;
    while (i <= j) {
        while (i <= right && arr[i] <= arr[pivot]) i++;
        while (j > left && arr[j] >= arr[pivot]) j--;
        if (i > j) [arr[pivot], arr[j]] = [arr[j], arr[pivot]];
        else [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    quickSort(arr, left, j - 1);
    quickSort(arr, j + 1, right);
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) {
    arr.push(Number(input[i]));
}

//mergeSort(arr, 0, n - 1);
quickSort(arr, 0, n - 1);

let answer = "";
for (let i = 0; i < arr.length; i++) {
    answer += arr[i] + "\n";
}
console.log(answer);

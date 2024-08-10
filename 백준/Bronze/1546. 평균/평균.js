// readline 모듈보다는 fs를 이용해 파일 전체를 읽어 들여 처리하기
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

// ["3", "40 80 60"]

let n = Number(input[0]); // 3
let arr = input[1].split(" ").map(Number); // [40, 80, 60]

let maxValue = -1;
for (let i = 0; i < n; i++) {
    maxValue = Math.max(maxValue, arr[i]);
}

let newArr = [];
for (let i = 0; i < n; i++) {
    newArr.push((arr[i] / maxValue) * 100);
}

let mean = 0;
for (let i = 0; i < n; i++) {
    mean += newArr[i];
}
mean /= n;
console.log(mean);
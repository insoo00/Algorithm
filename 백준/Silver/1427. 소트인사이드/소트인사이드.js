let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim();
let input = fs.readFileSync("/dev/stdin").toString().trim();

// let arr = [];
// for (let i=0; i<input.length; i++) {
//   arr.push(Number(input[i]));
// }

let arr = input.split('');


arr.sort((a,b) => b-a);


console.log(arr.join(""))

// // input값 처리
// const arr = require('fs').readFileSync('/dev/stdin').toString().trim().split('');



// sorted = arr.sort((a,b) => b - a);  // 내림차순 정렬

// sorted.join('');

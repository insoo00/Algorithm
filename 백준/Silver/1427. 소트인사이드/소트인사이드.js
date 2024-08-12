// input값 처리
const arr = require('fs').readFileSync('/dev/stdin').toString().trim().split('');

console.log(solution(arr));

function solution(arr) {
  sorted = arr.sort((a,b) => b - a);  // 내림차순 정렬

  return sorted.join('');
}
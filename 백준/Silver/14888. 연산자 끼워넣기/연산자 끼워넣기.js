let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 14888: 연산자 끼워넣기 
let n = Number(input[0]); // 수의 개수 
let arr = input[1].split(" ").map(Number); // 숫자 n개 
let op = input[2].split(" ").map(Number); // 덧셈, 뺄셈, 곱셈, 나눗셈 연산자의 개수 

// 만들 수 있는 식의 결과의 최대/최솟값 구하기 
let minResult = Infinity;
let maxResult = -Infinity;

// depth: 선택한 원소의 개수이자 재귀함수의 깊이 
function dfs(depth, curr) {
  if (depth === n - 1) { // 모든 숫자를 다 사용한 경우 
    minResult = Math.min(minResult, curr);
    maxResult = Math.max(maxResult, curr);
    return; 
  }

  // 각 연산자를 적용 
  for (let i = 0; i < 4; i++) {
    // 0: "+", 1: "-", 2: "*", 3: "/"
    if (op[i] > 0) { // 해당 연산자가 남아 있다면 
      op[i]--; // 연산자 사용
      let next;

      // 연산자에 따라 다음 값을 계산 
      if (i === 0) next = curr + arr[depth + 1];
      else if (i === 1) next = curr - arr[depth + 1];
      else if (i === 2) next = curr * arr[depth + 1];
      else { // i === 3 
        if (curr < 0) {
          curr = -curr;
          next = Math.floor(curr / arr[depth + 1]);
          next = -next;
        } else {
          next = Math.floor(curr / arr[depth + 1]);
        }
      }
        
      // 다음 깊이로 재귀함수 호출 
      dfs(depth + 1, next);
      op[i]++; // 사용한 연산자 되돌리기 
    }
  }
}

dfs(0, arr[0]);
console.log(maxResult === 0 ? 0 : maxResult);
console.log(minResult === 0 ? 0 : minResult);
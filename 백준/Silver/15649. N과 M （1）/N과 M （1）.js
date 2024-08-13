function dfs(cnt) {
  if (cnt == m) answer += arr.join(" ") + "\n";
  else {
    for (let i=1; i<n+1; i++) {
      if (arr.includes(i)) continue;
      arr.push(i);
      // console.log(arr);
      dfs(cnt+1);
      arr.pop();
    }
  }
}


let fs = require("fs");
// let [n, m] = fs.readFileSync("input.txt").toString().split(" ").map(Number);
let [n, m] = fs.readFileSync("/dev/stdin").toString().split(" ").map(Number);

// 1~4 중에서 중복 없이 2개 고르기
let arr = [];

let answer = "";
dfs(0);


console.log(answer);
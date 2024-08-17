function dfs(x) {
  // console.log(`x: ${x}`);
  visited[x] = true;
  answer += 1;
  for (i of graph[x]) {
    if (!visited[i]) {
        dfs(i);
    }
  }
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const m = Number(input[1]);
let graph = Array.from({ length: n + 1 }, () => []);
let visited = Array.from({ length: n + 1 }, () => false);

for (let i = 2; i < m + 2; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

answer = -1;
dfs(1);
console.log(answer);
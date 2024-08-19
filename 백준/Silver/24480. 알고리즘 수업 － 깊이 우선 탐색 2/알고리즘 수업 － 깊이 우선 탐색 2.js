let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, m, r] = input[0].split(" ").map(Number);
let graph = Array.from({ length: n + 1 }, () => []);
let visited = Array.from({ length: n + 1 }, () => 0);
let order = 1;

for (let i = 1; i < m + 1; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

for (let i = 1; i < n + 1; i++) {
  graph[i].sort((a, b) => b - a);
}

function dfs(cur) {
  visited[cur] = order++;

  for (next of graph[cur]) {
    if (visited[next] == 0) dfs(next);
  }
}

dfs(r);

let answer = "";
for (let i = 1; i < n + 1; i++) {
  answer += visited[i] + "\n";
}

console.log(answer);

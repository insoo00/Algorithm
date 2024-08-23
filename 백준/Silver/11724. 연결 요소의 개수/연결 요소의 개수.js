function dfs(x) {
  visited[x] = true;

  for (node of graph[x]) {
    if (!visited[node]) dfs(node);
  }
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, m] = input[0].split(" ").map(Number);
let graph = Array.from({ length: n + 1 }, () => []);
let visited = Array.from({ length: n + 1 }, () => false);

for (let i = 1; i < m + 1; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

let answer = 0;
for (let i = 1; i < n + 1; i++) {
  if (!visited[i]) {
    answer += 1;
    dfs(i);
  }
}

console.log(answer);

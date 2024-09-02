function dfs(x, y, depth) {
  visited[x] = true;
  // console.log(`x: ${x} y: ${y} depth: ${depth}, visited: ${visited}`);
  if (x == y) {
    answer = depth;
    return;
  }

  for (let g of graph[x]) {
    if (!visited[g]) {
      visited[g] = true;
      dfs(g, y, depth + 1);
    }
  }
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(input[0]);
const [x, y] = input[1].split(" ").map(Number);
const m = Number(input[2]);
let graph = Array.from({ length: n + 1 }, () => []);
let visited = Array.from({ length: n + 1 }, () => false);
for (let i = 3; i < m + 3; i++) {
  const [parent, child] = input[i].split(" ").map(Number);
  graph[parent].push(child);
  graph[child].push(parent);
}

let answer = -1;
dfs(x, y, 0);

console.log(answer);
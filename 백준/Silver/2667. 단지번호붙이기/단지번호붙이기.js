function dfs(x, y) {
  visited[x][y] = true;
  count += 1;

  for (let i=0; i<4; i++) {
    nx = x+dx[i];
    ny = y+dy[i];

    if (nx<0 || nx>=n || ny<0 || ny >=n) continue

    if (!visited[nx][ny] && map[nx][ny] === "1") dfs(nx, ny)
  }
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let map = [];
for (let i = 1; i < n + 1; i++) {
  map.push(input[i]);
}

let visited = [];
for (let i = 0; i < n; i++) {
  visited.push(Array.from({ length: n }, () => false));
}

let dx = [-1, 0, 1, 0];
let dy = [0, -1, 0, 1];

let total = 0;
let count = 0;
let result = [];

for (let i=0; i<n;i++) {
  for (let j=0; j<n; j++) {
    if (!visited[i][j] && (map[i][j] === "1")) {
      total += 1;
      count = 0;
      dfs(i, j);
      result.push(count);
    }
  }
}

console.log(total);
console.log(result.sort((a, b) => a-b).join("\n"));
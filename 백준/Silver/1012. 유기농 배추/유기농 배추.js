function dfs(x, y) {
  visited[x][y] = true;

  for (let i = 0; i < 4; i++) {
    nx = x + dx[i];
    ny = y + dy[i];

    if (nx < 0 || nx >= m || ny < 0 || ny > n) continue;

    if (!visited[nx][ny] && map[nx][ny] == 1) dfs(nx, ny);
  }
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const testCase = Number(input[0]);
let t = 0;
let m, n, k;
let map;
let visited;
let answer;

const dx = [-1, 0, 1, 0];
const dy = [0, -1, 0, 1];

let idx = 1;
while (t < testCase) {
  [m, n, k] = input[idx++].split(" ").map(Number);
  map = [];
  visited = [];
  answer = 0;
  for (let q = 0; q < m; q++) {
    map.push(Array.from({ length: n }, () => 0));
    visited.push(Array.from({ length: n }, () => 0));
  }
  for (let p = 0; p < k; p++) {
    const [x, y] = input[p + idx].split(" ").map(Number);
    map[x][y] = 1;
  }
  idx += k;

  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (!visited[r][c] && map[r][c] == 1) {
        dfs(r, c);
        answer += 1;
      }
    }
  }

  console.log(answer);
  t++;
}

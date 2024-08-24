class Queue {
  constructor() {
    this.items = {};
    this.headIndex = 0;
    this.tailIndex = 0;
  }
  enqueue(item) {
    this.items[this.tailIndex] = item;
    this.tailIndex++;
  }
  dequeue() {
    const item = this.items[this.headIndex];
    delete this.items[this.headIndex];
    this.headIndex++;
    return item;
  }
  peek() {
    return this.items[this.headIndex];
  }
  getLength() {
    return this.tailIndex - this.headIndex;
  }
}

function bfs(i, j, rain) {
  let q = new Queue();
  q.enqueue([i, j]);
  visited[i][j] = true;

  while (q.getLength()) {
    let [x, y] = q.dequeue();

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
      if (!visited[nx][ny] && graph[nx][ny] > rain) {
        visited[nx][ny] = true;
        q.enqueue([nx, ny]);
      }
    }
  }
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(input[i].split(" ").map(Number));
}
let visited;
let answer = -Infinity;

let dx = [-1, 0, 1, 0];
let dy = [0, -1, 0, 1];

for (let rain = 0; rain < 101; rain++) {
  visited = Array.from({ length: n }, () =>
    Array.from({ length: n }, () => false),
  );
  let cnt = 0;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (!visited[i][j] && graph[i][j] > rain) {
        bfs(i, j, rain);
        cnt++;
      }
    }
  }
  answer = Math.max(answer, cnt);
}

console.log(answer);

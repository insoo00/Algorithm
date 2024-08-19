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

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, m] = input[0].split(" ").map(Number);
let graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(input[i]);
}
let visited = Array.from({ length: n }, () =>
  Array.from({ length: m }, () => 0),
);

dx = [-1, 0, 1, 0];
dy = [0, -1, 0, 1];

let q = new Queue();
q.enqueue([0, 0]);
visited[0][0] = 1;

while (q.getLength()) {
  let [x, y] = q.dequeue();

  for (let i = 0; i < 4; i++) {
    nx = x + dx[i];
    ny = y + dy[i];

    if (nx < 0 || nx >= n || ny < 0 || ny > m) continue;
    if (visited[nx][ny] == 0 && graph[nx][ny] == "1") {
      q.enqueue([nx, ny]);
      visited[nx][ny] = visited[x][y] + 1;
    }
  }
}

console.log(visited[n - 1][m - 1]);

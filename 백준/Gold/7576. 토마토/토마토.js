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

const [m, n] = input[0].split(" ").map(Number);
let graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(input[i].split(" ").map(Number));
}
let total = n * m;
let cnt1 = 0;
let cnt2 = 0;
let answer = -Infinity;
let dx = [-1, 0, 1, 0];
let dy = [0, -1, 0, 1];

let q = new Queue();
for (let r = 0; r < n; r++) {
  for (let c = 0; c < m; c++) {
    if (graph[r][c] == 1) {
      q.enqueue([r, c]);
      cnt1++;
    } else if (graph[r][c] == -1) {
      cnt2++;
    }
  }
}

while (q.getLength()) {
  let [x, y] = q.dequeue();

  for (let i = 0; i < 4; i++) {
    nx = x + dx[i];
    ny = y + dy[i];

    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
    if (graph[nx][ny] == 0) {
      graph[nx][ny] = graph[x][y] + 1;
      answer = Math.max(answer, graph[nx][ny]);
      q.enqueue([nx, ny]);
      cnt1++;
    }
  }
}

if (cnt1+cnt2 == total) {
  answer = answer == -Infinity ? 1 : answer;
  console.log(answer-1);
  
} else {
  console.log(-1);
}

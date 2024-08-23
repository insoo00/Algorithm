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

function bfsNormal(node) {
  let [i, j] = node;
  let q = new Queue();
  q.enqueue([i, j]);
  visited[i][j] = 1;

  while (q.getLength()) {
    let [x, y] = q.dequeue();

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
      if (!visited[nx][ny]) {
        if (graph[nx][ny] == graph[x][y]) {
          visited[nx][ny] = visited[x][y];
          q.enqueue([nx, ny]);
        } 
      }
    }
  }
}

function checkRedGreen(target, source) {
  let [nx, ny] = target;
  let [x, y] = source;

  if (graph[nx][ny] == "R" && graph[x][y] == "G") return true;
  if (graph[nx][ny] == "G" && graph[x][y] == "R") return true;

  return false;
}

function bfsBlindness(node) {
  let [i, j] = node;

  let q = new Queue();
  q.enqueue([i, j]);
  visited[i][j] = 1;

  while (q.getLength()) {
    let [x, y] = q.dequeue();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
      if (!visited[nx][ny]) {
        if (graph[nx][ny] == graph[x][y] || checkRedGreen([nx, ny], [x, y])) {
          visited[nx][ny] = visited[x][y];
          q.enqueue([nx, ny]);
        } 
      }
    }
  }
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(input[i]);
}
let visited;
let dx = [-1, 0, 1, 0];
let dy = [0, -1, 0, 1];

let answerNoraml = 0;
visited = Array.from({ length: n }, () => Array.from({ length: n }, () => 0));
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (!visited[i][j]) {
      bfsNormal([i, j]);
      answerNoraml++;
    }
  }
}

let answerBlidness = 0;
visited = Array.from({ length: n }, () => Array.from({ length: n }, () => 0));
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (!visited[i][j]) {
      bfsBlindness([i, j]);
      answerBlidness++;
    }
  }
}

console.log(answerNoraml, answerBlidness);

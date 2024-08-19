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
const { nextTick } = require("process");
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

function bfs(x) {
  let q = new Queue();
  q.enqueue(x);
  visited[x] = order++;

  while (q.getLength()) {
    cur = q.dequeue();

    for (c of graph[cur]) {
      if (visited[c] == 0) {
        q.enqueue(c);
        visited[c] = order++;
      }
    }
  }
}

bfs(r);

let answer = "";
for (let i = 1; i < n + 1; i++) {
  answer += visited[i] + "\n";
}

console.log(answer);

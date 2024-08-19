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

const [n, m, v] = input[0].split(" ").map(Number);
let graph = Array.from({ length: n + 1 }, () => []);
let visited;
let answer;

for (let i = 1; i < m + 1; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

for (let i = 1; i < n + 1; i++) {
  graph[i].sort((a, b) => a - b);
}

function dfs(x) {
  answer.push(x);
  visited[x] = true;

  for (next of graph[x]) {
    if (visited[next] == false) dfs(next);
  }
}

function bfs(x) {
  let q = new Queue();
  q.enqueue(x);
  answer.push(x);
  visited[x] = true;

  while (q.getLength() != 0) {
    let cur = q.dequeue();

    for (next of graph[cur]) {
      if (visited[next] == false) {
        q.enqueue(next);
        answer.push(next);
        visited[next] = true;
      }
    }
  }
}

visited = Array.from({ length: n + 1 }, () => false);
answer = [];
dfs(v);
console.log(answer.join(" "));

visited = Array.from({ length: n + 1 }, () => false);
answer = [];
bfs(v);
console.log(answer.join(" "));

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

const n = Number(input[0]);
let graph = Array.from({length: n+1}, () => []);
let visited = Array.from({length: n+1}, () => false);
let answer = Array.from({length: n+1}, () => []);
for (let i=1; i<n; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

let q = new Queue();
q.enqueue(1);
visited[1] = true;
answer[1] = 1;

while (q.getLength()) {
  let cur = q.dequeue();

  for (let next of graph[cur]) {
    if(!visited[next]) {
      answer[next] = cur;
      visited[next] = true;
      q.enqueue(next);
    }
  }
}

answer = answer.slice(2,);
console.log(answer.join("\n"));
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

const [n, m, r] = input[0].split(" ").map(Number);
let graph = Array.from({length: n+1}, () => []);
let visited = Array.from({length: n+1}, () => false);
let answer = Array.from({length: n+1}, () => 0);
let order = 1;

for (let i=1; i<m+1; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

for (let i=1; i<n+1; i++) {
  graph[i].sort((a, b) => a-b);
}

function bfs(x) {
  q = new Queue();
  q.enqueue(x);
  visited[x] = true;

  while (q.getLength()) {
    cur = q.dequeue();
    visited[cur] = true;
    answer[cur] = order++;

    for (i of graph[cur]) {
      if (!visited[i]) {
        visited[i] = true;
        q.enqueue(i);
      }
    }
  }
}

bfs(r);
// console.log(answer);
console.log(answer.slice(1, ).join("\n"));
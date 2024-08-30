class Node {
  constructor(item) {
    this.item = item;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(item) {
    const node = new Node(item);
    if (this.head == null) {
      this.head = node;
      this.head.next = null;
    } else {
      this.tail.next = node;
    }

    this.tail = node;
    this.length += 1;
  }

  pop() {
    const popItem = this.head;
    this.head = this.head.next;
    this.length -= 1;
    return popItem.item;
  }

  size() {
    return this.length;
  }

  empty() {
    if (this.length == 0) {
      return 1;
    } else {
      return 0;
    }
  }

  front() {
    if (this.empty() == 1) return -1;
    return this.head.item;
  }

  back() {
    if (this.empty() == 1) return -1;
    return this.tail.item;
  }
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [n, k] = input[0].split(" ").map(Number);
let graph = [];

for (let i = 1; i < n + 1; i++) {
  graph.push(input[i].split(" ").map(Number));
}

const [s, aX, aY] = input[n + 1].split(" ").map(Number);

let visited = Array.from({ length: n }, () =>
  Array.from({ length: n }, () => 0),
);
let q = new Queue();
let candidates = [];
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (graph[i][j] != 0) {
      visited[i][j] = graph[i][j];
      candidates.push([graph[i][j], i, j]);
    }
  }
}

candidates.sort((a, b) => a[0] - b[0]);
for (let candidate of candidates) {
  q.push([...candidate, 0]);
}

dx = [-1, 0, 1, 0];
dy = [0, -1, 0, 1];

while (!q.empty()) {
  let [virus, x, y, time] = q.pop();

  if (time == s) break;
  for (let i=0; i<4; i++) {
    nx = x+dx[i];
    ny = y+dy[i];

    if (nx<0 || nx >=n || ny<0 || ny>=n) continue;
    if (visited[nx][ny] == 0) {
      visited[nx][ny] = virus;
      q.push([virus, nx, ny, time+1]);
    }
  }
}

console.log(visited[aX-1][aY-1]);
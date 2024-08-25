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

function bfs(i, j) {
  let q = new Queue();
  q.push([i, j]);
  visited[i][j] = true;

  while(!q.empty()) {
    let [x, y] = q.pop();

    for (let i=0; i<8; i++) {
      nx = x+dx[i];
      ny = y+dy[i];

      if(nx<0 || nx>=h || ny<0 || ny>=w) continue;
      if(graph[nx][ny] == 1 && !visited[nx][ny]) {
        q.push([nx, ny]);
        visited[nx][ny] = true;
      }
    }
  }
  
}
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let line = 0;
let w, h;
let graph;
let visited;

let dx = [-1, 0, 1, 0, -1, -1, 1, 1];
let dy = [0, -1, 0, 1, -1, 1, -1, 1]

while (!(input[line][0] == 0 && input[line][1] == 0)) {
  [w, h] = input[line++].split(" ").map(Number);
  graph = [];
  for (let i = 0; i < h; i++) {
    graph.push(input[line++].split(" ").map(Number));
  }
  visited = Array.from({ length: h }, () =>
    Array.from({ length: w }, () => false),
  );

  let answer = 0;
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (graph[i][j] == 1 && !visited[i][j]) {
        bfs(i, j);
        answer++;
      }
    }
  }
  console.log(answer);
}

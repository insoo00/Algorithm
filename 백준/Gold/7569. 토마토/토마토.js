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

const [M, N, H] = input[0].split(" ").map(Number);
let graph = Array.from({ length: H }, () =>
  Array.from({ length: N }, () => []),
);

let idx = 1;
for (let i = 0; i < H; i++) {
  for (let j = 0; j < N; j++) {
    graph[i][j] = (input[idx++].split(" ").map(Number));
  }
}

let q = new Queue();
let dx = [0, 0, -1, 0, 1, 0];
let dy = [0, 0, 0, -1, 0, 1];
let dz = [1, -1, 0, 0, 0, 0];
let cnt1 = 0;
let cnt2 = 0;
let total = H*M*N;
let answer = -Infinity;
for (let i=0; i<H; i++) {
  for (let j=0; j<N; j++) {
    for (let k=0; k<M; k++) {
      if (graph[i][j][k] == 1) {
        cnt1++;
        q.enqueue([i, j, k]);
      } else if (graph[i][j][k] == -1) {
        cnt2++;
      }
    }
  }
}

while (q.getLength()) {
  let [z, y, x] = q.dequeue();

  for (let i=0; i<6; i++) {
    nx = x+dx[i];
    ny = y+dy[i];
    nz = z+dz[i];

    if (nx<0 || nx>=M || ny<0 || ny >= N || nz<0 || nz>=H) continue;
    if (graph[nz][ny][nx] == 0) {
      graph[nz][ny][nx] = graph[z][y][x]+1;
      answer = Math.max(answer, graph[nz][ny][nx]);
      q.enqueue([nz, ny, nx]);
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
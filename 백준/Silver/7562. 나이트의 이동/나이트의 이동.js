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

const testCase = Number(input[0]);
let t = 0;
let idx = 1;

while (t < testCase) {
  let l = Number(input[idx++]);
  let [x, y] = input[idx++].split(" ").map(Number);
  let [tx, ty] = input[idx++].split(" ").map(Number);
  // let graph = [];
  // for (let i = 0; i < l; i++) {
  //   graph.push(Array.from({ length: l }, () => -1));
  // }
  let visited = [];
  for (let i = 0; i < l; i++) {
    visited.push(Array.from({ length: l }, () => -1));
  }

  let dx = [2, 1, -1, -2, -2, -1, 1, 2];
  let dy = [1, 2, 2, 1, -1, -2, -2, -1];

  let q = new Queue();
  q.enqueue([x, y]);
  visited[x][y] = 0;
  // graph[x][y] = 0;

  while (q.getLength()) {
    let [curX, curY] = q.dequeue();

    for (let i = 0; i < 8; i++) {
      nx = curX + dx[i];
      ny = curY + dy[i];

      if (nx < 0 || nx >= l || ny < 0 || ny >= l) continue;
      if (visited[nx][ny] == -1) {
        q.enqueue([nx, ny]);
        visited[nx][ny] = visited[curX][curY] + 1;
      }
    }
  }

  console.log(visited[tx][ty]);
  t++;
}

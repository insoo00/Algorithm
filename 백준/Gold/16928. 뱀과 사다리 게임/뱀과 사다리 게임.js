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

const [n, m] = input[0].split(" ").map(Number);
let line = 1;
let ladders = Array.from({length: 101}, () => -1);
let snakes = Array.from({length: 101}, () => -1);
let field = Array.from({length: 101}, () => -1);
for (let i=0; i<n; i++) {
  const [x, y] = input[line++].split(" ").map(Number);
  ladders[x] = y;
}
for (let i=0; i<m; i++) {
  const [u, v] = input[line++].split(" ").map(Number)
  snakes[u] = v;
}


let q = new Queue();
q.enqueue(1);
field[1] = 0;

while (q.getLength()) {
  let cur = q.dequeue();

  for (let move=1; move<7; move++) {
    let next = cur+move;

    if(next>100) continue;
    if(field[next] == -1) {
      field[next] = field[cur]+1;
      
      if (snakes[next] != -1) {
        field[snakes[next]] = field[snakes[next]] != -1 ? Math.min(field[snakes[next]], field[next]) : field[next];
        q.enqueue(snakes[next]);
      } else if (ladders[next] != -1) {
        field[ladders[next]] = field[ladders[next]] != -1 ? Math.min(field[ladders[next]], field[next]) : field[next];
        q.enqueue(ladders[next]);
      } else {
        q.enqueue(next);
      }
    }
  }
}
console.log(field[100]);
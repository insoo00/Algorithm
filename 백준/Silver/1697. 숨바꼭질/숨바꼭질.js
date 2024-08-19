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

const [n, k] = input[0].split(" ").map(Number);
let field = Array.from({ length: 100001 }, () => -1);

let q = new Queue();
q.enqueue(n);
field[n] = 0;

while (field[k] == -1) {
  let cur = q.dequeue();
  let nexts = [];
  nexts.push(cur - 1);
  nexts.push(cur + 1);
  nexts.push(cur * 2);

  for (next of nexts) {
    if (next < 0 || next > 100001) continue;
    if (field[next] == -1) {
      q.enqueue(next);
      field[next] = field[cur] + 1;
    }
  }
}

console.log(field[k]);

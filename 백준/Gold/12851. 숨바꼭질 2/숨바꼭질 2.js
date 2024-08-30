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
if (n >= k) {
  console.log(n - k);
  console.log(1);
  return;
}

let graph = Array.from({ length: k + 2 }, () => -1);
let answer = Array.from({ length: k + 2 }, () => 0);

let q = new Queue();
q.push(n);
graph[n] = 0;
answer[n] = 1;

while (!q.empty()) {
  let cur = q.pop();

  for (let next of [cur - 1, cur + 1, cur * 2]) {
    if (next < 0 || next > k + 1) continue;

    if (graph[next] == -1) {
      graph[next] = graph[cur] + 1;
      answer[next] += answer[cur]
      q.push(next);
    } else if (graph[next] == graph[cur] + 1) {
      answer[next] += answer[cur];
    }
  }
}



console.log(graph[k]);
console.log(answer[k]);

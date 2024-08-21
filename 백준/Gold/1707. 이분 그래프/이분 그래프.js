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

function toggle_flag(flag) {
  if (flag == 1) {
    return 2;
  } else {
    return 1;
  }
}

function dfs(x) {

  for (next of graph[x]) {
    if (!visited[next]) {
      visited[next] = toggle_flag(visited[x]);
      dfs(next);
    }
  }
}

function check_bipartite_graph(v) {
  for (let i = 1; i < v + 1; i++) {
    if (graph[i]) {
      for (node of graph[i]) {
        if (visited[i] == visited[node]) {
          return false;
        }
      }
    }
  }
  return true;
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let k = Number(input[0]);
let graph;
let visited;
let line = 1;
while (k) {
  const [v, e] = input[line++].split(" ").map(Number);
  graph = Array.from({ length: v + 1 }, () => []);
  visited = Array.from({ length: v + 1 }, () => false);
  for (let i = 0; i < e; i++) {
    const [u, v] = input[line++].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }
  for (let i = 1; i < v + 1; i++) {
    if (!visited[i]) {
      visited[i] = 1;
      dfs(i);
    }
  }
  if (check_bipartite_graph(v)) {
    console.log("YES");
  } else {
    console.log("NO");
  }
  k--;
}

let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let i = 0;
while(true) {
  const [a, b] = input[i].split(" ").map(Number);
  if ( (a==0) && (b==0) ) {
    break;
  } else {
    console.log(a+b);
  }
  i++;
}
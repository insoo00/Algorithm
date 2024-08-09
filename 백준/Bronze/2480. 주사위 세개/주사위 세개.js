let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split(" ");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

const [a, b, c] = input.map(Number);

if ((a==b) && (a==c)) {
  console.log(10000+a*1000);
} else if ((a==b) || (a==c)) {
  console.log(1000+a*100);
} else if ((b==a) || (b==c)) {
  console.log(1000+b*100);
} else {
  let num = Math.max(a, b, c);
  console.log(num*100);
}


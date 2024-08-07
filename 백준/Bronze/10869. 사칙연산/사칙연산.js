let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split(" ");
let input = fs.readFileSync('/dev/stdin').toString().split(' ')

let a = parseInt(input[0]);
let b = parseInt(input[1]);

let answer = "";
answer += a+b + "\n";
answer += a-b + "\n";
answer += a*b + "\n";
answer += parseInt(a/b) + "\n";
answer += a%b;

console.log(answer);

let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split(" ");
let input = fs.readFileSync("/dev/stdin").toString().split(" ")

let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

let answer = "";

answer += ((a + b) % c) + "\n";
answer += (((a % c) + (b % c)) % c) + "\n";
answer += (a*b)%c + '\n';
answer += ((a%c) * (b%c))%c;

console.log(answer);

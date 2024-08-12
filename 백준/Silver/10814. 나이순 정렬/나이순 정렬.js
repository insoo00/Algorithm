let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
let arr = new Array();
for (let i=1; i<n+1; i++) {
  arr.push({
    age: parseInt(input[i].split(" ")[0]),
    name: input[i].split(" ")[1]
   });
}

arr.sort((a,b) => a.age - b.age);

let answer = "";
for (let i=0; i<arr.length;i++) {
  answer += arr[i].age + " " + arr[i].name + "\n";
}

console.log(answer)
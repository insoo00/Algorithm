let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const distance = input[1].split(" ").map(Number);
const cost = input[2].split(" ").map(Number);


let hasDistance = 0;
let answer = 0;

for (let idx=0; idx<n-1; idx++) {
  if (idx!=0) hasDistance -= distance[idx-1];
  // console.log(`idx: ${idx}, hasDistance: ${hasDistance}`);  
  if (hasDistance==0) {
    let i = idx;
    if (cost[idx] > cost[idx+1]) {
      hasDistance += distance[idx];
      answer += cost[idx]*distance[idx];
      // console.log(`idx: ${idx}, hasDistance: ${hasDistance}, answer: ${answer}`);
    } else {
      while (cost[idx] <= cost[i] && i<n-1) {
        hasDistance += distance[i];
        answer += cost[idx]*distance[i]
        // console.log(`i: ${i}, hasDistance: ${hasDistance}, answer: ${answer}`);
        i++;
        
      }
    }
  } 
  
}

console.log(answer);
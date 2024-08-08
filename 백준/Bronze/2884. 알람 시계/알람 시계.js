let fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().split(" ");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");
// let input = fs.readFileSync(0, 'utf-8').trim().split('\n');


let hour = Number(input[0]);
let minute = Number(input[1]);

if (minute >= 45) {
  console.log(`${hour} ${minute-45}`)
} else {
  if (hour == 0) {
    console.log(`23 ${minute+15}`)
  } else {
    console.log(`${hour-1} ${minute+15}`)
  }
}


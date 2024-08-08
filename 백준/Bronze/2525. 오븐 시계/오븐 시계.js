let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [hour, minute] = input[0].split(" ").map(Number);
const time = Number(input[1]);

let tmpMin = minute+time

if (tmpMin < 60) {
  console.log(`${hour} ${tmpMin}`)
} else {
  let tmpHour = hour+parseInt(tmpMin/60)
  if (tmpHour >= 24) {
    tmpHour -= 24
  }
  console.log(`${tmpHour} ${tmpMin%60}`);
}


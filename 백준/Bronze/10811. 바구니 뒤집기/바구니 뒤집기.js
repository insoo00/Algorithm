const fs = require('fs'); 
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [count, line] = input[0].split(' ').map(Number);
let baskets = Array(count).fill(1).map((v, i) => v + i); // count길이 만큼의 배열을 생성하여 1로 채운 후, map을 돌면서 요소마다 인덱스 + 1한 값을 반환

for (let i = 1; i <= line; i++) {
    let [start, end] = input[i].split(' ').map(Number);// 입력의 두번째 줄 부터의 요소를 split후 map으로 숫자 타입 변환 후 각각 start와 end에 할당
    let reversedPart = baskets.slice(start - 1, end).reverse(); // 만들어놓은 baskets 배열에 slice 메서드를 이용해 start - 1 (주어진 숫자는 1부터 시작하지만 배열은 0부터 시작하기 때문)부터 end까지 자르고 뒤집은 후 변수에 반환 
    baskets.splice(start - 1, end - start + 1, ...reversedPart); // splice 메서드로 시작 인덱스부터 자를 개수 (만약 start가 2이고 end가 5면 실제 1,2,3,4번째 인덱스 네 개를 잘라야 하므로 5 - 2 + 1를 해야 4를 얻을 수 있음.), 그 안을 대체할 reversedPart 레스트 연산자를 세번째 매개변수로 입력
}

// 결과 출력
console.log(baskets.join(' ')); // 출력은 문자열이여야 하므로 join으로 합친 후 출력.
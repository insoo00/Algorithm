function quickSort(arr, left, right) {
    if (left >= right) {
        // 원소가 2개 이상일 때만 수행
        return;
    }
    // [3, 5, 6, 8, 9]
    //        l     r
    // right - left + 1 => 3이 나옴
    //
    let pivot = Math.floor(Math.random() * (right - left + 1)); // [0, 원소 개수)에서 추출
    // 0, 1, 2 중에 하나 고르게 됨.
    pivot += left; // 2, 3, 4 중에 하나 고르게 됨
    // let pivot = right;
    [arr[pivot], arr[left]] = [arr[left], arr[pivot]];
    pivot = left;
    let i = left + 1;
    let j = right;
    while (i <= j) {
        // 왼쪽에서는 pivot보다 큰 데이터를 찾음
        while (i <= right && arr[i] <= arr[pivot]) i++;
        // 오른쪽에서는 pivot보다 작은 데이터를 찾음
        while (j > left && arr[j] >= arr[pivot]) j--;
        // 엇갈렸다면 pivot이랑 j이랑 교체
        if (i > j) [arr[pivot], arr[j]] = [arr[j], arr[pivot]];
        // 엇갈리지 않았다면 i와 j를 교체
        else [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    // 여기까지 오면, pivot을 기준으로 작은 데이터는 모두 왼쪽에, 큰 건 모두 오른
    // 왼쪽과 오른쪽을 기준으로 각각 마찬가지로 정렬 수행
    quickSort(arr, left, j - 1);
    quickSort(arr, j + 1, right);
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) {
    arr.push(Number(input[i]));
}

quickSort(arr, 0, arr.length - 1);

let answer = "";
for (let i = 0; i < arr.length; i++) {
    answer += arr[i] + "\n";
}
console.log(answer);

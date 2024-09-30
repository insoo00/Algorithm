import sys

input = sys.stdin.readline

n = int(input())
inputs = input().split()

# 팩토리얼 값을 저장하는 dp 배열
dp = [1] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] * i

# 첫 번째 소문제 (k번째 순열 구하기)
if inputs[0] == '1':
    idx = int(inputs[1])
    nums = list(range(1, n + 1))  # 순열을 만들기 위해 리스트로 생성
    res = []

    idx -= 1  # 0-index 기반으로 처리

    for i in range(n, 0, -1):
        fact = dp[i - 1]
        pos = idx // fact
        res.append(nums.pop(pos))  # 해당 위치의 숫자를 결과에 추가
        idx %= fact  # 남은 순열 인덱스 업데이트

    print(' '.join(map(str, res)))

# 두 번째 소문제 (몇 번째 순열인지 구하기)
else:
    data = list(map(int, inputs[1:]))
    nums = list(range(1, n + 1))  # 순열을 만들기 위한 리스트
    offset = 0

    for i in range(n):
        num = data[i]
        pos = nums.index(num)  # 현재 숫자가 있는 위치를 찾아서
        offset += pos * dp[n - i - 1]  # 해당 위치에 해당하는 순열의 개수를 더함
        nums.pop(pos)  # 해당 숫자를 리스트에서 제거

    print(offset + 1)  # 1-index 기반이므로 최종적으로 +1을 해줌
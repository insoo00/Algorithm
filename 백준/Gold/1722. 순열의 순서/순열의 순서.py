import sys

input = sys.stdin.readline

n = int(input())
inputs = input().split()

dp = [1] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] * i

if inputs[0] == '1':
    idx = int(inputs[1])
    nums = set([i for i in range(1, n+1)])
    res = []
    offset = 0

    for length in range(n):
        index = 0
        for num in nums:
            index += 1
            if idx <= offset + index * dp[n-length-1]:
                offset += (index -1) * dp[n-length-1]
                res.append(num)
                nums.remove(num)
                break
    print(*res)

else:
    data = list(map(int, inputs[1:]))
    nums = [i for i in range(1, n+1)]
    offset = 1

    for d in data:
        cnt = 0
        for num in nums:
            if num < d:
                cnt += 1
            else:
                break
        offset += cnt * dp[len(nums)-1] 
        nums.remove(d)

    print(offset)
T = int(input())
for case in range(1, T+1):
    nums = list(map(int, input().split()))
    result = 0
    for num in nums:
        result += num
    result = int(round(result/len(nums), 0))

    print(f'#{case} {result}')
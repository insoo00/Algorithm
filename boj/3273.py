n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

res = 0
left, right = 0, n-1
while left < right:
    tmp = nums[left] + nums[right]
    if tmp == x:
        res += 1
        left += 1
    elif tmp < x:
        left += 1
    else:
        right -= 1
print(res)

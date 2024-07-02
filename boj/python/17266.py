N = int(input())
M = int(input())
x = list(map(int, input().split()))

result = 0

if len(x) == 1:
    result = max(x[0]-0, N-x[0])
else:
    for i in range(len(x)):
        if i == 0:
            height = x[i] - 0
        elif i == len(x) - 1:
            height = N - x[i]
        else:
            tmp = x[i] - x[i-1]
            if tmp % 2:
                height = tmp // 2 + 1
            else:
                height = tmp // 2
        result = max(height, result)

print(result)
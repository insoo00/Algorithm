n = int(input())

time = list(map(int, input().split()))

sorted_time = sorted(time)

result = [0] * len(sorted_time)
result[0] = sorted_time[0]

for i in range(1, len(sorted_time)):
    result[i] = result[i-1] + sorted_time[i]

print(sum(result))
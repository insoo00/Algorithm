n, x = map(int, input().split())
visitors = list(map(int, input().split()))

intervalSum = 0
for i in range(x):
    intervalSum += visitors[i]
max = intervalSum
cnt = 1

for start in range(0, n-x):
    end = start+x
    intervalSum -= visitors[start]
    intervalSum += visitors[end]

    # print(f'max: {max} intervalSum: {intervalSum}')
    if max == intervalSum:
        cnt += 1
    elif intervalSum > max:
        max = intervalSum
        cnt = 1

if max == 0:
    print("SAD")
else: 
    print(max)
    print(cnt)

    
    
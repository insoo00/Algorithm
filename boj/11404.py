from collections import deque
N = int(input())
M = int(input())
MAX_COST = int(1e9)
dp = [[MAX_COST for _ in range(N+1)] for _ in range(N+1)] 
for i in range(N+1):
    dp[i][i] = 0

for _ in range(M):
    start, end, cost = map(int, input().split())
    dp[start][end] = min(dp[start][end], cost)


for k in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            dp[start][end] = min(dp[start][end], dp[start][k] + dp[k][end])


for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] == MAX_COST:
            print("0", end=" ")
        else:
            print(dp[i][j], end=" ")
    print()

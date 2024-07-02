# 2839
INF = float('inf')
N = int(input())
dp = [INF for _ in range(N+1)]

for i in range(1, N+1):
    if i == 3 or i ==5:
        dp[i] = 1
    elif i > 5:
        dp[i] = min(dp[i-3], dp[i-5]) + 1

result = dp[N]
if result == INF:
    print(-1)
else:
    print(result)

N, K = map(int, input().split())
dp = [0]*(K+1)
for _ in range(N):
    W, V = map(int, input().split())
    if W > K:
        continue
    # for i in range(W, K+1):
    # 뒤에서부터 비교를 해줘야 (W, V)가 중복되는 것을 방지할 수 있음
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W]+V)

print(dp[K])

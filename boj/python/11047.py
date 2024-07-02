N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

coin_idx = N
result = 0

for coin in coins[::-1]:
    if K//coin > 0:
        result += K//coin
        K = K%coin

print(result)

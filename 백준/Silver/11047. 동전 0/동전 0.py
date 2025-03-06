N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

result = 0
for coin in reversed(coins):
    if K//coin != 0:
        result += K//coin
        K = K%coin
    
print(result)

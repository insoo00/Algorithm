N, M = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

start = max(money)
end = sum(money)
result = 0

while start <= end:
    mid = (start+end)//2

    cnt = 0
    budget = 0
    for m in money:
        if budget < m:
            cnt += 1
            budget = mid
        budget -= m

    if cnt <= M:
        result = mid
        end = mid-1
    else:
        start = mid+1

print(result)

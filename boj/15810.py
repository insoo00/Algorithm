N, M = map(int, input().split())
info = list(map(int, input().split()))

low, high = 1, min(info)*M

while low <= high:
    mid = (low+high)//2
    cnt = 0
    for i in range(N):
        cnt += mid//info[i]

    if cnt < M:
        low = mid+1
    else:
        high = mid-1

print(low)
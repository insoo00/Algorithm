K, N = map(int, input().split())
lans = []
for _ in range(K):
    lans.append(int(input()))

start, end = 1, max(lans)

while start <= end:
    mid = (start+end)//2
    print(f'start: {start}, end: {end}, mid: {mid}')
    cnt = 0

    for lan in lans:
        cnt += lan//mid

    print(f'cnt: {cnt}')
    if cnt >= N:
        start = mid+1
    else:
        end = mid-1

print(end)
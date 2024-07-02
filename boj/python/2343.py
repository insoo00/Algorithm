N, M = map(int, input().split())
lectures = list(map(int, input().split()))

start, end = max(lectures), sum(lectures)

while start<=end:
    mid = (start+end)//2
    # print(f'start: {start}, end: {end}, mid: {mid}')

    cnt = 1
    tmp_sum = 0
    for lecture in lectures:
        tmp_sum += lecture
        if tmp_sum > mid:
            tmp_sum = lecture
            cnt += 1

    # print(f'cnt: {cnt}')
    if cnt > M:
        start = mid+1
    else:
        end = mid-1

print(start)

# start: 1 
# 반례
# 5 4
# 1 5 9 3 10

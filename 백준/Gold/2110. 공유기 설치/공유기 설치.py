N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

start = 1
end = houses[-1]-houses[0]
result = -1

while start <= end:
    mid = (start+end)//2            # 두 공유기 사이의 거리

    cnt = 1                         # 공유기 설치 대수 (첫 번째 집 설치 시작)
    cur = houses[0]                 # 현재 공유기 설치한 집
    for house in houses:            # 다음 공유기 설치 가능한 집 찾기
        if house - cur >= mid:
            cnt += 1
            cur = house
        
    if cnt >= C:                    # 공유기 다 설치함 -> 거리를 벌려야됨
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)

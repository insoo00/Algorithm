# 2667
from collections import deque

def bfs(i, j):
    global res, dx, dy, houses
    q = deque()
    q.append((i, j))
    houses[i][j] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if houses[nx][ny]:
                houses[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    res.append(cnt)


N = int(input())
houses = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []

for i in range(N):
    for j in range(N):
        if houses[i][j]:
            bfs(i, j)

print(len(res))

res.sort()
for r in res:
    print(r)

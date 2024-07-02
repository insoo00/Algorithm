# 7576

from collections import deque

def bfs(q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

bfs(q)

res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)

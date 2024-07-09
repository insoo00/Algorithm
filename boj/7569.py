# 7569

from collections import deque

def bfs(q):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if nx<0 or nx>=H or ny<0 or ny>=N or nz<0 or nz>=M:
                continue

            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z]+1
                q.append((nx, ny, nz))


M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

bfs(q)

res = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)            
        res = max(res, max(j))
print(res-1)

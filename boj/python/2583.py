#bfs
from collections import deque

def bfs(x, y):
    global areas
    
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    area = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and visited[nx][ny]==False:
                visited[nx][ny] = True
                q.append([nx, ny])
                area += 1
    areas.append(area)


M, N, K = map(int, input().split())
visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(K):
    lb_x, lb_y, rt_x, rt_y = map(int, input().split())
    for r in range(lb_x, rt_x):
        for c in range(lb_y, rt_y):
            visited[c][r] = True

cnt = 0
areas = list()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for r in range(M):
    for c in range(N):
        if visited[r][c] == False:
            cnt += 1
            bfs(r, c)

areas.sort()
print(cnt)
print(*areas)

# dfs
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global area
    
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<M and 0<=ny<N and visited[nx][ny]==False:
            area += 1
            dfs(nx, ny)

M, N, K = map(int, input().split())
boxes = list()
for _ in range(K):
    boxes.append(list(map(int, input().split())))

visited = [[False for _ in range(N)] for _ in range(M)]
for box in boxes:
    lb_x, lb_y, rt_x, rt_y = box[0], box[1], box[2], box[3]
    for r in range(lb_x, rt_x):
        for c in range(lb_y, rt_y):
            visited[c][r] = True

cnt = 0
areas = list()
area = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for r in range(M):
    for c in range(N):
        if visited[r][c] == False:
            cnt += 1
            dfs(r, c)
            areas.append(area)
            area = 1

areas.sort()
print(cnt)
print(*areas)

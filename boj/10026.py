from collections import deque

N = int(input())
field = list()
for _ in range(N):
    field.append(list(input()))
normal, non_normal = 0, 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque()

def bfs(x, y):
    q.append((x,y))
    visited[x][y] = True
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if field[nx][ny] == field[cur_x][cur_y]:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))

visited = [[False]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            bfs(x,y)
            normal += 1

for x in range(N):
    for y in range(N):
        if field[x][y] == 'G':
            field[x][y] = 'R'

visited = [[False]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            bfs(x,y)
            non_normal += 1

print(normal, non_normal)


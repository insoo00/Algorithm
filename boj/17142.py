from collections import deque
from itertools import combinations

INF = float('inf')

def bfs(q, cnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited = [[False for _ in range(N)] for _ in range(N)]

    time = 0

    while True:
        if cnt == 0 or len(q) == 0:
            if cnt == 0:
                return time
            else:
                return INF

        time += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            visited[x][y] = True

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue

                if not visited[nx][ny]:
                    if field[nx][ny] == 0:
                        visited[nx][ny] = True
                        cnt -= 1
                        q.append((nx, ny))
                    elif field[nx][ny] == 2:
                        visited[nx][ny] = True
                        q.append((nx, ny))

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

virus_info = []
cnt = 0

for i in range(N):
    for j in range(N):
        if field[i][j]==0:
            cnt += 1
        elif field[i][j]==2:
            virus_info.append((i, j))

virus_candidates = combinations(virus_info, M)
res = INF

for virus_candidate in virus_candidates:
    q = deque()
    for virus in virus_candidate:
        q.append(virus)
    
    tmp_res = bfs(q, cnt)
    res = min(res, tmp_res)

if res == INF:
    print(-1)
else:
    print(res)


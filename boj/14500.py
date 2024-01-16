import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_val = max(map(max, field))

def dfs(x, y, dept, sum_val):
    global result
    if dept==4:
        result = max(result, sum_val)
        return
    if max_val*(4-dept)+sum_val <= result:
        return
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
                visited[nx][ny] = True
                if dept==2:
                    dfs(x, y, 3, sum_val+field[nx][ny])
                dfs(nx, ny, dept+1, sum_val+field[nx][ny])
                visited[nx][ny] = False

result = 0
for x in range(N):
    for y in range(M):
        visited[x][y] = True
        dfs(x, y, 1, field[x][y])
        visited[x][y] = False
print(result)
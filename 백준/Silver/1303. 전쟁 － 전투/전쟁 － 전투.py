def dfs(x, y, cnt):
    color = table[x][y]
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < m and 0 <= ny < n) and not visited[nx][ny]:
            if(table[nx][ny] == color):
                cnt = dfs(nx, ny, cnt + 1)
    return cnt

        
n, m = map(int, input().split())

table = []
visited = [[False for _ in range(n)] for _ in range(m)]
for _ in range(m):
    table.append(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

w_cnt = 0
b_cnt = 0

for i in range(m):
  for j in range(n):
    if not visited[i][j]:
        if(table[i][j] == 'W'):
            w_cnt += (dfs(i, j, 1))**2
        elif(table[i][j] == 'B'):
            b_cnt += (dfs(i, j, 1))**2

print(w_cnt, b_cnt)
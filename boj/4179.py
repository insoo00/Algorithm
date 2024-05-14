from collections import deque

            
R, C = map(int, input().split())
maze = list()
for _ in range(R):
    maze.append(list(input()))

q = deque()
for i in range(R):
    for j in range(C):
        if maze[i][j] == "J":
            q.append((0, i, j))
for i in range(R):
    for j in range(C):
        if maze[i][j] == "F":
            q.append((-1, i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = "IMPOSSIBLE"

while q:
    current, x, y = q.popleft()

    if current != -1:
        if maze[x][y] != "F":
            if x==0 or y==0 or x==R-1 or y==C-1:
                res = current + 1
                break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 

        if 0<=nx<R and 0<=ny<C and maze[nx][ny] != "#":
            if current != -1 and maze[nx][ny] == ".":
                maze[nx][ny] = "J"
                q.append((current+1, nx, ny))

            elif current == -1 and maze[nx][ny] != "F":
                maze[nx][ny] = "F"
                q.append((-1, nx, ny))

print(res)

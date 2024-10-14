n,m = map(int,input().split())
graph = []
r,c,d = map(int,input().split())

# 북(0) -> 동(1) -> 남(2) -> 서(3)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

graph[r][c] = 2
cnt = 1

while True:
    cleanup = False
    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3)%4
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            cnt += 1
            r = nx
            c = ny
            cleanup = True
            break
    if not cleanup:
        if graph[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]
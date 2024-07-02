from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    field[i][j] == 0

    while q:
        a, b = q.popleft()

        positions = [[a+1, b], [a-1, b], [a, b+1], [a, b-1]]

        for pos in positions:
            x_pos = pos[0]
            y_pos = pos[1]
            if x_pos<0 or y_pos<0 or x_pos>=x or y_pos>=y:
                continue
            if field[x_pos][y_pos] == 1:
                q.append((x_pos, y_pos))
                field[x_pos][y_pos] = 0

T = int(input())
for _ in range(T):
    x, y, cnt = map(int, input().split())
    field = [[0] * y for _ in range(x)]
    for _ in range(cnt):
        dx, dy = (map(int, input().split()))
        field[dx][dy] = 1

    result = 0 
    for i in range(x):
        for j in range(y):
            if field[i][j] == 1:
                bfs(i, j)
                result +=1
    
    print(result)




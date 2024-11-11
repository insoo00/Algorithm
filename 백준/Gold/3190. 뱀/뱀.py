from collections import deque
n = int(input())
k = int(input())

# 0: 빈칸, 1: 뱀, 2: 사과
field = [[0 for _ in range(n)] for _ in range(n) ] 
for _ in range(k):
    x, y = map(int, input().split())
    field[x-1][y-1] = 2
l = int(input())
d_info = {}
for _ in range(l):
    time, dir = input().split()
    d_info[int(time)] = dir

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
x, y = 0, 0
field[x][y] = 1
q = deque([(x, y)])
cnt = 0

def turn(alpha):
    global d
    if alpha == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4

while True:
    cnt += 1
    x, y = x+dx[d], y+dy[d]

    # 벽
    if x<0 or x>=n or y<0 or y>=n:
        break

    # 사과 있음
    if field[x][y] == 2:
        field[x][y] = 1
        q.append((x, y))
        if cnt in d_info:
            turn(d_info[cnt])
    
    # 사과 없음
    elif field[x][y] == 0:
        field[x][y] = 1
        q.append((x, y))
        nx, ny = q.popleft()
        field[nx][ny] = 0
        if cnt in d_info:
            turn(d_info[cnt])
        
    # 자기자신의 몸과 부딪힘
    else:
        break

print(cnt)
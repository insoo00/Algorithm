import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

field = [[None for _ in range(N)]]

for i in range(N):
    colors = [None]
    colors.extend(map(int, input().split()))
    field.append(colors)

def cnt(x, y):
    global blue, white
    if field[x][y] == 1:
        blue += 1
    else:
        white += 1

def validation_color(x, y, N):
    color = field[x][y]
    for i in range(x-N+1, x+1):
        for j in range(y-N+1, y+1):
            if color != field[i][j]:
                return True
    cnt(x, y)
    return False

def recursive(x, y, N):
    if N == 1:
        cnt(x, y)
        return
    if not validation_color(x, y, N):
        return
    
    N = N//2
    recursive(x, y, N)
    recursive(x, y-N, N)
    recursive(x-N, y, N)
    recursive(x-N, y-N, N)

blue = 0
white = 0
recursive(N, N, N)
print(white, blue, sep='\n')
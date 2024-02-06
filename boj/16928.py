import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ladders = dict()
snakes = dict()
for _ in range(N):
    a, b = map(int, input().split())
    ladders[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

board = [0]*101
visited = [False]*101

def dfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        pos = q.popleft()

        for num in range(1,7):
            current = pos+num
            if current > 100:
                break
            if not visited[current]:
                if current in ladders.keys():
                    current = ladders[current]
                elif current in snakes.keys():
                    current = snakes[current]
                
                if not visited[current]:
                    q.append(current)
                    visited[current] = True
                    board[current] = board[pos]+1
                
dfs(1)
print(board[100])
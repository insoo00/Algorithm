import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX_RANGE = 10**5
visited = [0] * (MAX_RANGE+1)

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        current = q.popleft()

        if current == K:
            return visited[current]
        for i in (current-1, current+1, current*2):
            if 0<=i<=MAX_RANGE and visited[i]==0:
                visited[i] = visited[current] + 1
                q.append(i)

print(bfs(N))
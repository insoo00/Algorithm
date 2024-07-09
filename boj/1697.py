#dp
N, K = map(int, input().split())
MAX = 10**5

dp = [MAX] * (K+1)

if N >= K:
    print(N-K)
    exit()

for i in range(N):
    dp[i] = N-i

dp[N] = 0

for i in range(N+1, K+1):
    if i%2==0:
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    else:
        dp[i] = min(dp[i-1] + 1, dp[(i+1)//2] + 2)

print(dp[K])

#bfs
from collections import deque

N, K = map(int, input().split())

def bfs(N):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(field[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=10**5 and field[nx]==0:
                field[nx] = field[x]+1
                q.append(nx)

field = [0]*(10**5+1)
bfs(N)

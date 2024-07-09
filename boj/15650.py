#1
from itertools import combinations

N, M = map(int, input().split())
S = [_ for _ in range(1, N+1)]
tmp = combinations(S, M)
tmp_list = list(tmp)

for item in tmp_list:
    for i in item:
        print(i, end=" ")
    print()

#2
N, M = map(int, input().split())
visited = [False]*(N+1)
result = []

def DFS(depth, start):
    if depth == M:
        print(' '.join(map(str, result)))
    else:
        for next in range(start+1, N+1):
            if not visited[next]:
                visited[next] = True
                result.append(next)
                DFS(depth+1, next)
                visited[next] = False
                result.pop()
    return

DFS(0, 0)

import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
answer = [0]*(N+1)
order = 1

for _ in range(M):
  u, v= map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for list in graph:
  list.sort()


def dfs(v):
  global order
  # print(f'v: {v}')
  visited[v] = True
  answer[v] = order
  order += 1

  for i in graph[v]:
    if not visited[i]:
      # print(f'v, i, order: {v}, {i}, {order}')
      dfs(i)


dfs(start)

for i in range(1, N+1):
  print(answer[i])
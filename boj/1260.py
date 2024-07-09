# 1260
from collections import deque

def dfs(start):
    global visited
    print(start, end=" ")
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)

def bfs(start):
    global visited
    visited[start] = True
    q = deque([start])

    while q:
        current = q.popleft()
        print(current, end=" ")
        for node in graph[current]:
            if not visited[node]:
                q.append(node)
                visited[node] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False for _ in range(N+1)]
dfs(V)

print()

visited = [False for _ in range(N+1)]
bfs(V)



# from collections import defaultdict, deque
# from copy import deepcopy

# def dfs(N, V, graph):
# # 1: [2, 3, 4] 
# # 2: [1, 4]
# # 3: [1, 4]
# # 4: [1, 2, 3]
    
#     q = deque()
#     visited = [False]*(N+1)
#     q.append(graph[V])
#     visited[V] = True
#     result = []
#     result.append(V)

#     while q:
#         x = q.popleft()
#         print(q)
#         if x not in visited:
#             q.append(graph[x])
#             visited[x] = True
#             result.append(x)

#     return result


# def bfs(V, graph):
#     pass

# N, M, V = map(int, input().split())
# graph = defaultdict(list)

# for _ in range(M):
#     left, right = map(int, input().split())
#     graph[left].append(right)
#     graph[right].append(left)

# print(dfs(N, V, deepcopy(graph)))
# print(bfs(N, V, graph))

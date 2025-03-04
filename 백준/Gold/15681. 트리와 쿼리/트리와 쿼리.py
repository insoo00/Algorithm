import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
tree = [[] for _ in range(N+1)]
parents = [[] for _ in range(N+1)]
result = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split()) 
    graph[U].append(V)
    graph[V].append(U)

def makeTree(current, parent):
    for child in graph[current]:
        if child != parent:
            tree[current].append(child)
            parents[child] = current
            makeTree(child, current)

def countSubtreeNodes(current):
    result[current] = 1
    for child in tree[current]:
        countSubtreeNodes(child)
        result[current] += result[child]

makeTree(R, -1)
countSubtreeNodes(R)

for _ in range(Q):
    q = int(input())
    print(result[q])

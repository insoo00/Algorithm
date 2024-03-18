N, M = map(int, input().split())
result = []

def DFS(depth):
    if depth == M:
        print(' '.join(map(str, result)))
    else:
        for next in range(1, N+1):
            result.append(next)
            DFS(depth+1)
            result.pop()
    return

DFS(0)

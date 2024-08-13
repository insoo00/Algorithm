N, M = map(int, input().split())
result = []

def DFS(depth, start):
    if depth == M:
        print(' '.join(map(str, result)))
    else:
        for next in range(start, N+1):
            result.append(next)
            DFS(depth+1, next)
            result.pop()
    return

DFS(0, 1)

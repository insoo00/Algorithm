N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()
result = []

def DFS(depth, start):
    if depth == M:
        print(' '.join(map(str, result)))
    else:
        for next in range(start, N):
            result.append(N_list[next])
            DFS(depth+1, next+1)
            result.pop()
    return

DFS(0, 0)

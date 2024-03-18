N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()
visited = [False]*N
result = []

def DFS(depth):
    if depth == M:
        print(' '.join(map(str, result)))
    else:
        for next in range(N):
            if not visited[next]:
                visited[next] = True
                result.append(N_list[next])
                DFS(depth+1)
                visited[next] = False
                result.pop()
    return

DFS(0)

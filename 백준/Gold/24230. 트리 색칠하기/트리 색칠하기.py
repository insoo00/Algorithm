import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def dfs(node, color):
    global ans
    
    for child_node in trees[node]:
        if not visited[child_node]:
            visited[child_node] = True
            # print(f'node: {node} child_node: {child_node}')
            if colors[child_node] != color:
                ans += 1
                # print(f'ans: {ans}')
            dfs(child_node, colors[child_node])



n = int(input())
colors = [0] + list(map(int, input().split()))
trees = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    trees[u].append(v)
    trees[v].append(u)

ans = 0
visited[1] = True
dfs(1, colors[1])

if colors[1] != 0:
    ans += 1
print(ans)

from collections import defaultdict, deque
import copy

N = int(input())
data = defaultdict(list)
for idx in range(1, N+1):
    data[int(input())].append(idx)
result = set()

def dfs(num):
    tmp_data = copy.deepcopy(data)
    q = deque(tmp_data[num])
    visited = [False]*(N+1)
    visited[num] = True

    while q:
        tmp = set([num])
        cur = q.pop()
        for x in tmp_data[cur]:
            if not visited[x]:
                q.append(x)
                visited[x] = True
                tmp.add(x)
            else:
                if num == x:
                    result.add(num)
                if x in tmp:
                    result.add(x)

for val in data:
    dfs(val)

ans = list(result)
ans.sort()

print(len(ans))
for re in ans:
    print(re, end='\n')
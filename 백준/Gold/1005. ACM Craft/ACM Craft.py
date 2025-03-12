import sys
input = sys.stdin.readline

def calc_time(end):
    max_time = float('-inf')
    for start in info[end]:
        if result[start] == -1:
            calc_time(start)
        max_time = max(max_time, result[start])
    
    if max_time == float('-inf'):
        result[end] = times[end]
    else:
        result[end] = max_time+times[end]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0]
    times.extend(list(map(int, input().split())))
    info = [[] for _ in range(N+1)]
    result = [-1 for _ in range(N+1)]

    for _ in range(K):
        s, e = map(int, input().split())
        info[e].append(s)
    final = int(input())

    calc_time(final)
    print(result[final])

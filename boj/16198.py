def dfs(energy, marbles):
    # print(f'energy: {energy}, marbles: {marbles}')
    global res
    cnt = len(marbles)
    if cnt == 2:
        res = max(res, energy)
    else:
        for i in range(1, cnt-1):
            tmp_energy = marbles[i-1] * marbles[i+1]
            tmp_marbles = marbles[:i]+marbles[i+1:]
            dfs(energy+tmp_energy, tmp_marbles)


N = int(input())
marbles = list(map(int, input().split()))

res = 0
dfs(0, marbles)
print(res)
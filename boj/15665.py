def dfs(depth):
    global permutations

    if depth == M:
        print(*permutations)
        return

    for num in nums:
        permutations.append(num)
        dfs(depth+1)
        permutations.pop()

N, M = map(int, input().split())
nums = sorted(list(set(list(map(int, input().split())))))

permutations = list()
dfs(0)

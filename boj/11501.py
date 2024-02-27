T = int(input())
for _ in range(T):
    N = int(input())
    costs = list(map(int, input().split()))
    result = 0
    max_cost = costs[-1]
    for cost in costs[::-1]:
        if cost >= max_cost:
            max_cost = cost
        else:
            result += max_cost-cost

    print(result)

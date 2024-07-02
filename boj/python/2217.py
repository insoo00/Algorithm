N = int(input())
weights = []
for _ in range(N):
    weights.append(int(input()))
weights.sort()

result = -1
for idx, weight in enumerate(weights):
    result = max(result, weight*(N-idx))
print(result)

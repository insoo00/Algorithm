N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort()

result = -1
for idx, rope in enumerate(ropes):
    result = max(result, rope*(N-idx))
print(result)

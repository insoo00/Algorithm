import sys

input = lambda: sys.stdin.readline().rstrip()
a = int(input())
b = int(input())

prime = [0 for _ in range(b+1)]
for i in range(2, b+1):
    for j in range(1, b+1):
        if i*j <= b:
            prime[i*j] += 1
        else:
            break

result = list()
for i in range(a, b+1):
    if prime[i] == 1:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
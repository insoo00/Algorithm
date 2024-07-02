import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
X = list(map(int, input().split()))
X_set = sorted(set(X))
X_dict = dict()
for idx, val in enumerate(X_set):
    X_dict[val] = idx

for i in X:
    print(X_dict[i], end=" ")
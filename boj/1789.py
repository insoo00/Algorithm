import sys

input = lambda: sys.stdin.readline().rstrip()
S = int(input())
N = 1
tmp = N
while tmp <= S:
    N += 1
    tmp += N
if N == 1:
    print(N)
else:
    print(N-1)

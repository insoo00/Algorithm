import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
permutation = list(map(int, input().split()))
operator = list(map(int, input().split()))

def dfs(dept, val):
    global operator, max_val, min_val
    if dept==N:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    else:
        if operator[0]: # add
            operator[0] -= 1
            dfs(dept+1, val+permutation[dept])
            operator[0] += 1
        if operator[1]: # subtract
            operator[1] -= 1
            dfs(dept+1, val-permutation[dept])
            operator[1] += 1
        if operator[2]: # multiply
            operator[2] -= 1
            dfs(dept+1, val*permutation[dept])
            operator[2] += 1
        if operator[3]: # divide
            operator[3] -= 1
            dfs(dept+1, int(val/permutation[dept]))
            operator[3] += 1

max_val = int(-1e9)
min_val = int(1e9)
dfs(1, permutation[0])
print(max_val)
print(min_val)
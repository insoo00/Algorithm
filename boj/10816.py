import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

count = dict()
for N_element in N_list:
    if N_element in count:
        count[N_element] += 1
    else:
        count[N_element] = 1

for M_element in M_list:
    result = count.get(M_element)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
        
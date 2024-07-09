
# 2776
T = int(input())

for _ in range(T):
    N = int(input())
    N_set = set(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))

    for M_element in M_list:
        if M_element in N_set:
            print(1)
        else:
            print(0)

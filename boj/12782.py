T = int(input())
for _ in range(T):
    N, M = input().split()
    result = 0
    zero = 0
    one = 0
    for i in range(len(M)):
        if N[i] != M[i]:
            if M[i] == '1':
                one += 1
            else:
                zero += 1
    result = max(one, zero)
    print(result)

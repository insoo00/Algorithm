S = input()

flag = -1
zero_cnt = 0
one_cnt = 0
for num in S:
    if num != flag:
        flag = num
        if num == '0':
            zero_cnt += 1
        else:
            one_cnt += 1
        
result = min(zero_cnt, one_cnt)
print(result)

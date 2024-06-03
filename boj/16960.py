N, M = map(int, input().split())
lamps = [0 for _ in range(M+1)]
lamps[0] = 1
switch_info = list()
for _ in range(N):
    switch_tmp = list(map(int, input().split()))
    for i in range(1, len(switch_tmp)):
        lamps[switch_tmp[i]] += 1
    switch_info.append(switch_tmp)
    

flag = False
for switch in switch_info:
    for i in range(1, len(switch)):
        lamps[switch[i]] -= 1
    
    if 0 not in lamps:
        flag = True
        break

    for i in range(1, len(switch)):
        lamps[switch[i]] += 1

if flag == True:
    print(1)
else:
    print(0)

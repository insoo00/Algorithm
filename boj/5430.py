from collections import deque

T = int(input())

def stringToDeque(data):
    return deque(data.strip('[]').split(','))

for _ in range(T):
    command = input().replace('RR', '')
    length = int(input())
    if length != 0:
        data = stringToDeque(input())
    else:
        input()
        data = deque()
    flag = False
    R_cnt = 0
    for com in command:
        if com == 'R':
            R_cnt += 1
        if com == 'D':
            if len(data) == 0:
                flag = True
                break
            else:
                if R_cnt%2 == 0:
                    data.popleft()
                else:
                    data.pop()
    
    if flag == True:
        print('error')
    else:
        if R_cnt%2 == 0:
            print('['+','.join(data)+']')
        else:
            data.reverse()
            print('['+','.join(data)+']')
# https://school.programmers.co.kr/learn/courses/20848/lessons/255904

from collections import deque

def mov(pos, dir, com):
    x = pos[0]
    y = pos[1]
    if dir[0] == 'x':
        if dir[1] == '+':
            if com == 'G':
                return [x+1, y]
            else:
                return [x-1, y]
        else:
            if com == 'G':
                return [x-1, y]
            else:
                return [x+1, y]
    else:
        if dir[1] == '+':
            if com == 'G':
                return [x, y+1]
            else:
                return [x, y-1]
        else:
            if com == 'G':
                return [x, y-1]
            else:
                return [x, y+1]

        
def solution(command):
    dir = deque([['y', '+'], ['x', '+'], ['y', '-'], ['x', '-']])
    answer = [0, 0]
    
    for com in command:
        if com == 'G' or com == 'B':
            answer = mov(answer, dir[0], com)
        elif com == 'R':
            dir.rotate(-1)
        elif com == 'L':
            dir.rotate(1)
    
    return answer

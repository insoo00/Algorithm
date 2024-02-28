# https://school.programmers.co.kr/learn/courses/20847/lessons/255902

from collections import deque

def solution(queries):
    answer = []
    
    for query in queries:
        info = deque()
        gen = query[0]-1
        pea = query[1]-1
        while gen>0:
            info.appendleft([pea//4, pea%4])
            gen -= 1
            pea = pea//4
            
        result = deque(["Rr"])
        for i in range(len(info)):
            if result[i] == "RR":
                result.append("RR")
            elif result[i] == "rr":
                result.append("rr")
            else:
                if info[i][1] == 0:
                    result.append("RR")
                elif info[i][1] == 3:
                    result.append("rr")
                else:
                    result.append("Rr")
        answer.append(result.pop())         
    return answer

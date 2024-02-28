# https://school.programmers.co.kr/learn/courses/20848/lessons/255905

import heapq

def solution(ability, number):
    heapq.heapify(ability)
    for _ in range(number):
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)
        heapq.heappush(ability, a+b)
        heapq.heappush(ability, a+b)
    
    answer = sum(ability)
    return answer
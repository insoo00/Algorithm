# https://school.programmers.co.kr/learn/courses/20847/lessons/255901

import itertools
   
def solution(ability):
    answer = 0
    student_cnt = [_ for _ in range(len(ability))]
    event_cnt = len(ability[0])
    for permutation in list(itertools.permutations(student_cnt, event_cnt)):
        tmp=0
        for idx, val in enumerate(permutation):
            tmp += ability[val][idx]
        if tmp > answer:
            answer = tmp
        
    return answer

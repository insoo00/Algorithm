# https://school.programmers.co.kr/learn/courses/20847/lessons/255900

def solution(input_string):
    answer_list = list()
    alpha_set = set()
    prev_string = ''
    for alpha in input_string:
        if alpha != prev_string:
            if alpha in alpha_set:
                if alpha not in answer_list:
                    answer_list.append(alpha)
            else:
                alpha_set.add(alpha)
        prev_string = alpha
    answer_list.sort()
    
    answer = ''
    if answer_list:
        for item in answer_list:
            answer += item
    else:
        answer = 'N'
        
    return answer
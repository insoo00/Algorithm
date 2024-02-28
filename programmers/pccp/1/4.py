# https://school.programmers.co.kr/learn/courses/20847/lessons/255903

def solution(program):
    answer = [0 for _ in range(11)]
    program.sort(key=lambda x:(x[0], x[1]))
    time = 0
    while program:
        for pro in program:
            if pro[1] <= time:
                answer[pro[0]] += time-pro[1]
                time += pro[2]
                program.remove(pro)
                break

    answer[0] = time
    return answer
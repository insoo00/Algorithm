# https://school.programmers.co.kr/learn/courses/20848/lessons/255906

def solution(menu, order, k):
    answer, waiting = 0, 0
    making_time = [0]
    for i in order:
        making_time.append(making_time[-1] + menu[i])
    del making_time[0]
    
    customer = list()
    for i in range(1, len(order)):
        customer.append(i*k)
        
    print(making_time, customer)
    
    
        
    for time in range(making_time[-2]):
        if time%k==0 and time <len(order)*k:
            waiting += 1
        if time in making_time[1:]:
            waiting -= 1
        answer = max(answer, waiting)
    
    return answer

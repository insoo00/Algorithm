switch_cnt = int(input())
switch_status = [-1]
switch_status.extend(list(map(int, input().split())))
student_cnt = int(input())
student_list = list()
for _ in range(student_cnt):
    student_list.append(list(map(int, input().split())))

def toggle(left, right):
    global switch_status
    for num in range(left, right+1):
        switch_status[num] = 1 if switch_status[num] == 0 else 0

for student in student_list:
    sex = student[0]
    num = student[1]
    if sex == 1:
        base = num
        while num <= switch_cnt:
            switch_status[num] = 1 if switch_status[num] == 0 else 0
            num += base
    else:
        left = num-1
        right = num+1
        if num<=1 or num>=switch_cnt:
            switch_status[num] = 1 if switch_status[num] == 0 else 0
            continue
        while (switch_status[left] == switch_status[right]):
            left -= 1
            right += 1
            if left<1 or right>switch_cnt:
                break
        toggle(left+1, right-1)

for idx, status in enumerate(switch_status[1:], 1):
    if idx%20 == 0:
        print(status)
    else:
        print(status, end=" ")
def solution(users, emoticons):
    answer = [0, 0]
    discount_rate = [10, 20, 30, 40]
    discounts = []

    def dfs(temp, depth):
        if depth == len(temp):
            discounts.append(temp[:])
            return
        for rate in discount_rate:
            temp[depth] += rate
            dfs(temp, depth + 1)
            temp[depth] -= rate

    dfs([0 for _ in range(len(emoticons))], 0)
    

    for discount in discounts:
        plus = 0
        cost = 0

        for user in users:
            buy = 0
            for idx, emoticon in enumerate(emoticons):
                if discount[idx] >= user[0]:
                    buy += emoticon * ((100 - discount[idx]) / 100)
            if user[1] <= buy:
                plus += 1
            else:
                cost += buy

        if plus >= answer[0]:
            if plus == answer[0]:
                answer[1] = max(answer[1], cost)
            else:
                answer[1] = cost
            answer[0] = plus
            
    return answer
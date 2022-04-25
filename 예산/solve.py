def solution(d, budget):
    answer = 0

    while d != []:
        price = min(d) # price of product which is going to be supported
        if budget < price:
            break
        budget -= price
        answer += 1
        d.remove(price)

    return answer
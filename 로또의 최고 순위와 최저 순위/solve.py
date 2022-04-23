def solution(lottos, win_nums):
    answer = [0, 0]
    correct = 0 # how many correct numbers in lottos
    zero = 0 # how many 0s in lottos


    # calculate the lowest ranking

    for n in lottos:
        if n == 0:
            zero += 1
        if n in win_nums:
            correct += 1
    
    if correct <= 1:
        answer[1] = 6
    else:
        answer[1] = 7 - correct

    
    # calculate the highest ranking

    answer[0] = answer[1] - zero
    if answer[0] < 1:
        answer[0] = 1


    return answer
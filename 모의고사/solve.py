def solution(answers):
    # calculate supoja1's score
    supoja1_score = 0
    for prob_num in range(len(answers)):
        if answers[prob_num] == prob_num % 5 + 1:
            supoja1_score += 1

    # calculate supoja2's score
    supoja2_score = 0
    for prob_num in range(len(answers)):
        if prob_num % 2 == 0:
            if answers[prob_num] == 2:
                supoja2_score += 1
        elif prob_num % 8 == 1 or prob_num % 8 == 3:
            if answers[prob_num] == prob_num % 8:
                supoja2_score += 1
        elif prob_num % 8 == 5:
            if answers[prob_num] == 4:
                supoja2_score += 1
        elif prob_num % 8 == 7:
            if answers[prob_num] == 5:
                supoja2_score += 1

    # calculate supoja3's score
    supoja3_score = 0
    for prob_num in range(len(answers)):
        if prob_num % 10 == 0 or prob_num % 10 == 1:
            if answers[prob_num] == 3:
                supoja3_score += 1
        elif prob_num % 10 == 2 or prob_num % 10 == 3:
            if answers[prob_num] == 1:
                supoja3_score += 1
        elif prob_num % 10 == 4 or prob_num % 10 == 5:
            if answers[prob_num] == 2:
                supoja3_score += 1
        elif prob_num % 10 == 6 or prob_num % 10 == 7:
            if answers[prob_num] == 4:
                supoja3_score += 1
        elif prob_num % 10 == 8 or prob_num % 10 == 9:
            if answers[prob_num] == 5:
                supoja3_score += 1

    # get answer
    answer = [1, 2, 3]
    if supoja1_score < supoja2_score or supoja1_score < supoja3_score:
        answer.remove(1)
    if supoja2_score < supoja1_score or supoja2_score < supoja3_score:
        answer.remove(2)
    if supoja3_score < supoja1_score or supoja3_score < supoja2_score:
        answer.remove(3)

    return answer
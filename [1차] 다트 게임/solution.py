import string

def solution(dartResult):
    dartResult_arr = []

    # split dartResult to each set
    # ex) 1S2D*3T -> ['1S', '2D*', '3T']
    prev_idx = 0
    for idx in range(len(dartResult)):
        if idx == len(dartResult) - 1:
            dartResult_arr.append(dartResult[prev_idx:])
        elif dartResult[idx] not in string.digits and dartResult[idx + 1] in string.digits:
            dartResult_arr.append(dartResult[prev_idx:idx + 1])
            prev_idx = idx + 1

    # split each set to score, bonus, option
    # ex) '2D*' -> [2, 'D', '*']
    for idx in range(len(dartResult_arr)):
        tmp_arr = []
        for i in range(len(dartResult_arr[idx])):
            if dartResult_arr[idx][i] in string.digits and dartResult_arr[idx][i + 1] not in string.digits:
                tmp_arr.append(int(dartResult_arr[idx][:i + 1])) # score
            elif dartResult_arr[idx][i] in string.digits:
                continue
            else:
                tmp_arr.append(dartResult_arr[idx][i])
        if len(tmp_arr) == 2: # no option
            tmp_arr.append('')
        dartResult_arr[idx] = tmp_arr

    # calculate score
    answer = 0
    prev_score = 0
    score = 0
    for s in dartResult_arr:
        score = s[0]
        bonus = s[1]
        option = s[2]

        # bonus
        if bonus == 'D':
            score *= score
        elif bonus == 'T':
            score *= score * score
        
        # option
        if option == '*':
            prev_score *= 2
            score *= 2
        elif option == '#':
            score *= -1

        answer += prev_score
        prev_score = score
        score = 0
    
    answer += prev_score

    return answer
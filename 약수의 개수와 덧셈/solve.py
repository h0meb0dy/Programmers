def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        if n == (int(n ** (1/2))) ** 2: # if n is square
            answer -= n
        else:
            answer += n

    return answer
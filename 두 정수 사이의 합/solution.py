def solution(a, b):
    answer = 0

    if a < b:
        for n in range(a, b + 1):
            answer += n
    else:
        for n in range(b, a + 1):
            answer += n

    return answer
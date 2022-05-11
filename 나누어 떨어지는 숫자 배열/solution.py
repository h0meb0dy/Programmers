def solution(arr, divisor):
    answer = []
    
    for number in arr:
        if number % divisor == 0:
            answer.append(number)

    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer
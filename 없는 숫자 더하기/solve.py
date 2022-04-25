def solution(numbers):
    exist = {number: False for number in range(10)} # if n exists in numbers, exist[n] = True

    for number in numbers:
        exist[number] = True

    answer = 0

    for number in range(10):
        if exist[number] == False:
            answer += number
            
    return answer
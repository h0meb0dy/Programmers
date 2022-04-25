def solution(numbers):
    answer = []

    for idx1 in range(len(numbers)):
        for idx2 in range(idx1 + 1, len(numbers)):
            sum_result = numbers[idx1] + numbers[idx2]
            if sum_result not in answer:
                answer.append(sum_result)

    answer.sort()

    return answer
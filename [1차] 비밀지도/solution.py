def solution(n, arr1, arr2):
    total_map = [0 for i in range(n)]

    for i in range(n):
        total_map[i] = arr1[i] | arr2[i]

    answer = []

    for i in range(n):
        # ex) 0b011001 -> ' ##  #'
        answer.append(bin(total_map[i])[2:].rjust(n, ' ').replace('1', '#').replace('0', ' '))

    return answer
def solution(n):
    n_ternary = '' # n expressed in ternary scale

    while n != 0:
        n_ternary += str(n % 3)
        n = int(n / 3)

    return int(n_ternary, 3)
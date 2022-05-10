def solution(n):
    divider = 1

    while 1:
        if n % divider == 1:
            return divider
        else:
            divider += 1
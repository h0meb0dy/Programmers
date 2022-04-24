def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for num in range(10):
        s = s.replace(numbers[num], str(num)) # zero -> '0', one -> '1', ..., nine -> '9'

    answer = int(s) # '1234' -> 1234
    
    return answer
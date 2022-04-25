# calculate distance between key1 and key2
def distance(key1, key2):
    return abs(key2[0] - key1[0]) + abs(key2[1] - key1[1])

def solution(numbers, hand):
    position = {'*': (0, 0), '0': (1, 0), '#': (2, 0), '7': (0, 1), '8': (1, 1), '9': (2, 1), '4': (0, 2), '5': (1, 2), '6': (2, 2), '1': (0, 3), '2': (1, 3), '3': (2, 3)} # {key: coordinate}

    l_position = position['*'] # initial position of left hand
    r_position = position['#'] # initial position of right hand

    answer = ''

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L' # 1, 4, 7 -> left hand
            l_position = position[str(number)]
            continue
        elif number == 3 or number == 6 or number == 9:
            answer += 'R' # 3, 6, 9 -> right hand
            r_position = position[str(number)]
            continue

        l_distance = distance(l_position, position[str(number)]) # distance between left hand and key to tab
        r_distance = distance(r_position, position[str(number)]) # distance between right hadn and key to tab

        if l_distance < r_distance:
            answer += 'L'
            l_position = position[str(number)]
            continue
        elif l_distance > r_distance:
            answer += 'R'
            r_position = position[str(number)]
            continue

        if hand == 'left':
            answer += 'L'
            l_position = position[str(number)]
        else:
            answer += 'R'
            r_position = position[str(number)]
    
    return answer
import string

def step(new_id):
    answer = new_id

    # step 1: change all letters to lowercase
    answer = answer.lower()

    # step 2: remove letters which are not allowed (allowed: alphabet, number, '-', '_', '.')
    allowed = string.ascii_lowercase + string.digits + '-' + '_' + '.' # allowed characters
    tmp = answer
    for c in tmp:
        if c not in allowed:
            answer = answer.replace(c, '')

    # step 3: remove continuous periods
    while 1:
        new = answer.replace('..', '.')
        if new == answer:
            break
        answer = new
    
    # step 4: remove first/last period
    if len(answer) >= 2 and answer[len(answer) - 1] == '.':
        answer = answer[:-1]
    if len(answer) >= 1 and answer[0] == '.':
        answer = answer[1:]
    
    # step 5: change empty id to "a"
    if answer == '':
        answer = 'a'

    # step 6: make id shorter than 16
    if len(answer) >= 16:
        answer = answer[:15]

    # step 7: make id longer than 2
    while len(answer) <= 2:
        answer += answer[len(answer) - 1]

    return answer

def solution(new_id):
    while 1:
        answer = step(new_id)
        if answer == new_id:
            return answer
        new_id = answer

if __name__ == '__main__':
    print(solution('...!@BaT#*..y.abcdefghijklm'))
    print(solution('z-+.^.'))
    print(solution('=.='))
    print(solution('123_.def'))
    print(solution('abcdefghijklmn.p'))
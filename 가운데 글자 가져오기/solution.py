def solution(s):
    s_len = len(s) # length

    if s_len % 2 == 0: # if length is even
        return s[int(s_len / 2) - 1:int(s_len / 2) + 1]
    else: # if length is odd
        return s[int((s_len - 1) / 2)]
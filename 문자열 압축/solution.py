def solution(s):
    s_len = len(s)
    answer = s_len

    for sub_len in range(1, int(s_len / 2) + 1):
        sliced_arr = []
        
        # slice string
        idx = 0
        while s_len - idx >= sub_len:
            sliced_arr.append(s[idx:idx + sub_len])
            idx += sub_len
        sliced_arr.append(s[idx:])
        
        # compress sliced string
        sliced_str = ''
        loop = 1
        substr = sliced_arr[0]
        for i in range(1, len(sliced_arr)):
            if sliced_arr[i] == substr:
                loop += 1
            else:
                if loop != 1:
                    sliced_str += str(loop)
                loop = 1
                sliced_str += substr
                substr = sliced_arr[i]
        
        if loop != 1:
            sliced_str += str(loop)
        sliced_str += substr

        if len(sliced_str) < answer:
            answer = len(sliced_str)

    return answer
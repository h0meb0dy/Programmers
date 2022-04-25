def solution(board, moves):
    bucket = [] # bucket for selected dolls
    answer = 0 # the number of popped dolls

    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                doll = row[move - 1] # select doll
                row[move - 1] = 0 # remove doll from board
                bucket.append(doll) # put the doll in bucket

                if len(bucket) >= 2 and bucket[-1] == bucket[-2]: # if two same dolls are selected continuously
                    bucket.pop()
                    bucket.pop()
                    answer += 2 # pop both of the dolls
                
                break # next move

    return answer
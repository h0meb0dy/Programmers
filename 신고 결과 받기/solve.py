def solution(id_list, reports, k):
    n = len(id_list) # the number of users
    report_matrix = [[False for i in range(n)] for i in range(n)] # if id_list[i] is reported by id_list[j], report_matrix[i][j] = True
    answer = [0 for i in range(n)] # how many mails each user receives


    # fill report_matrix

    for report in reports:
        report_pair = report.split() # 'muzi frodo' -> ['muzi', 'frodo']
        reporter_user = report_pair[0]
        reported_user = report_pair[1]
        reporter_user_idx = id_list.index(reporter_user)
        reported_user_idx = id_list.index(reported_user)
        report_matrix[reported_user_idx][reporter_user_idx] = True

    
    # calculate how many mails each user receives

    for reported_user_idx in range(n):
        reported_times = report_matrix[reported_user_idx].count(True) # how many times each user is reported
        if reported_times >= k: # if a user is reported more than k times, that user is banned
            for reporter_user_idx in range(n):
                if report_matrix[reported_user_idx][reporter_user_idx] == True:
                    answer[reporter_user_idx] += 1


    return answer
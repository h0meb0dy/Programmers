def solution(N, stages):
    failure_rate = [-1 for stage in range(N + 1)] # failure_rate[i] == failure rate of stage i
    challenging_user = [0 for stage in range(N + 1)] # challenging_user[i] == the number of users who are challenging to stage i
    not_challenging_user = 0 # the number of users who are challenging to previous stages

    for i in range(1, N + 1):
        challenging_user[i] = stages.count(i) # the number of users who are challenging to stage i
        if len(stages) - not_challenging_user == 0:
            failure_rate[i] = 0 # if no one reached at stage i, failure rate is 0
        else:
            failure_rate[i] = float(challenging_user[i]) / float(len(stages) - not_challenging_user) # failure rate of stage i
        not_challenging_user += challenging_user[i]

    answer = []

    for i in range(N):
        stage = failure_rate.index(max(failure_rate)) # stage failure rate of which is highest
        answer.append(stage)
        failure_rate[stage] = -1
    
    return answer
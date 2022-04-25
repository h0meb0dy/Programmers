def solution(participant, completion):
    participant_dict = {hash(participant[idx]): participant[idx] for idx in range(len(participant))} # {hash: participant}

    participant_sum = 0
    for athlete in participant:
        participant_sum += hash(athlete) # sum of hashes of all participants

    completion_sum = 0
    for athlete in completion:
        completion_sum += hash(athlete) # sum of hashes of participants who completed race

    difference = participant_sum - completion_sum # hash of participant who didn't complete race

    return participant_dict[difference]
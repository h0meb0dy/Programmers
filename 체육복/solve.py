def solution(n, lost, reserve):
    students = [1 for idx in range(n)]
    for lost_idx in lost:
        students[lost_idx - 1] -= 1 # students who lost clothes
    for reserve_idx in reserve:
        students[reserve_idx - 1] += 1 # students who have extra clothes

    # lend / borrow
    for idx in range(len(students) - 1):
        if (students[idx] == 2 and students[idx + 1] == 0) or (students[idx] == 0 and students[idx + 1] == 2):
            students[idx] = 1
            students[idx + 1] = 1
            idx += 1

    return students.count(1) + students.count(2)
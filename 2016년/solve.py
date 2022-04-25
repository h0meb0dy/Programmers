def solution(a, b):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    days = 0 # days between 2016/01/01 and 2016/a/b
    for month in range(1, a):
        days += month_days[month - 1]
    days += b - 1

    return week_days[(5 + days) % 7] # 2016/01/01 is week_days[5]
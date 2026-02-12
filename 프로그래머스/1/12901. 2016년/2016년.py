def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    tmp = 0
    for m in month[:a-1]:
        tmp += m
    tmp += b-1
    tmp = tmp%7 # 하나빼야됨

    return day[tmp]
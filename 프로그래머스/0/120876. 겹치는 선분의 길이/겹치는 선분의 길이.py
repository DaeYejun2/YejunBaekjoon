def solution(lines):
    res = 0
    for i in range(-100, 101):
        if (lines[0][0] <= i < lines[0][1]) and (lines[1][0] <= i < lines[1][1]): res += 1
        elif (lines[1][0] <= i < lines[1][1]) and (lines[2][0] <= i < lines[2][1]): res += 1
        elif (lines[0][0] <= i < lines[0][1]) and (lines[2][0] <= i < lines[2][1]): res += 1
    return res

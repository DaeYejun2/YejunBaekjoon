def solution(s):
    first = s[0]
    tmp = 1
    cnt = 0
    res = 0
    for i in range(1, len(s)):
        if tmp == cnt: 
            res += 1
            tmp = 0; cnt = 0
            first = s[i]
            print(first)
        if s[i] == first: tmp += 1
        else: cnt += 1

    return res+1
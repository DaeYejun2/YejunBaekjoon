def solution(n, m, section):
    cnt = 0
    last = 0
    for s in section:
        if last < s:
            cnt += 1
            last = s + m - 1
    return cnt
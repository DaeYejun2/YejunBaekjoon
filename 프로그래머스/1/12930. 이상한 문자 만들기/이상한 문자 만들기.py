def solution(s):
    s = s.split(' ')
    res = []
    for i in range(len(s)):
        tmp = ''
        for j, a in enumerate(s[i]):
            if j % 2: tmp += a.lower()
            else: tmp += a.upper()
        res.append(tmp)

    return ' '.join(res)
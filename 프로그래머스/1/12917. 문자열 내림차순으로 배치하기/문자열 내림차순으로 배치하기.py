def solution(s):
    s = [ord(i) for i in s]
    s = sorted(s, reverse=True)
    res = ''
    for i in s:
        res+=chr(i)
    return res
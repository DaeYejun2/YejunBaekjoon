def solution(a, b):
    if a > b: a,b=b,a
    res = a
    for i in range(a+1, b+1):
        res += i
    return res
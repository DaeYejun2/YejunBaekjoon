def solution(a, b, n):
    tmp = 0
    res = 0
    while n >= a:
        e = (n // a)*b
        res += e
        n = n%a + e
        
    return res
def gcd(a, b):
    if a == 0: return b
    return gcd(b%a, a)

def solution(n, m):
    return [gcd(n, m), (n*m) // gcd(n,m)]
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

def solution(numer1, denom1, numer2, denom2):
    lcm = denom1 * denom2 // gcd(denom1, denom2)
    n1 = lcm // denom1; n2 = lcm // denom2
    a, b = n1*numer1 + n2*numer2, lcm
    v = gcd(a, b)
    if v == 0: return [a, b]
    else: return [a//v, b//v]
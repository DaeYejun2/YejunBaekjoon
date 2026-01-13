n = int(input())
d = [0] * (n+1)

def dp(n):
    if n == 1: return 1
    if n == 2: return 2
    if d[n] != 0: return d[n]
    d[n] = dp(n-1) + dp(n-2)
    return d[n]
    
print(dp(n) % 10007)
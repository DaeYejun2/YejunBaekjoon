import sys
input = sys.stdin.readline

n, k = map(int, input().split())
m = 1000000007

def factorial(num, mod):
    res = 1
    for i in range(2, num+1):
        res = (res * i) % mod
    return res

top = factorial(n, m)

bottom = (factorial(k, m) * factorial(n-k, m)) % m

print((top * pow(bottom, m-2, m))%m)
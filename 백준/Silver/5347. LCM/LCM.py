import sys
input = sys.stdin.readline

def gcd(a, b):
    if a == 0: return b
    return gcd(b%a, a)

t = int(input())

for _ in range(t):
    a, b = map(int,input().split())
    print((a*b)//gcd(a,b))
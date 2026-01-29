import sys
input = sys.stdin.readline

def power(a, b, m):
    if b == 0: return 1
    tmp = power(a,b//2,m)

    if b % 2 == 0: return (tmp*tmp)%m
    else: return (tmp*tmp*a)%m

for _ in range(int(input())):
    a,b=map(int,input().split())
    p=power(a,b,10)
    if p == 0: print(10)
    else: print(p)
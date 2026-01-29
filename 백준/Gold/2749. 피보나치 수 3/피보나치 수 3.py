import sys
input = sys.stdin.readline

def pisano(m):
    a, b = 0, 1
    for i in range(m*m):
        a,b=b,(a+b)%m
        if a == 0 and b == 1:
            return i+1

m = 1000000
p = pisano(m)
n=int(input())
rn = n%p
if rn<=1:
    res=rn
else:
    a, b = 0, 1
    for i in range(rn-1):
        a, b = b, (a+b)%m
    res = b

print(res)
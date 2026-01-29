import sys
input = sys.stdin.readline
m = 1000000007
def pow(a, b, m):
    if b == 0: return 1

    tmp = pow(a, b//2, m)

    if b%2==0:
        return (tmp*tmp)%m
    else:
        return (tmp*tmp*a)%m
    
a = int(input())
x = int(input())
print(pow(a,x,m))
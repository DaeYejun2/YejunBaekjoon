import sys
input = sys.stdin.readline
# b를 절반씩 줄이면서

a, b, c = map(int, input().split())

def POW(a, b):
    if b == 1:
        return a % c
    else:
        tmp = POW(a, b // 2)
        if b % 2:  #홀수면
            return (tmp * tmp * a) % c
        else:      #짝수면
            return (tmp * tmp) % c

print(POW(a, b))
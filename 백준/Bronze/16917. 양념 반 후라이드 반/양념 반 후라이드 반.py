import sys
input = sys.stdin.readline

a, b, c, x, y = map(int, input().split())

if c*2 < a+b:
    if x > y:
        tmp = c*2 * y
        if (x-y)*a > (x-y)*2*c:
            tmp += (x-y)*2*c
        else:
            tmp += (x-y)*a
    else:
        tmp = c*2 * x
        if (y-x)*b > (y-x)*2*c:
            tmp += (y-x)*2*c
        else:
            tmp += (y-x)*b
        
    print(tmp)
        
else:
    print(a*x + b*y)
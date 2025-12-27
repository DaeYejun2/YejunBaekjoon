import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    s = input().rstrip()
    first = []; second = []
    le = len(s)
    if le == 1: 
        first = s; second = s
        print(''.join(first))
        print(''.join(second))
        continue
    if le % 2:    #홀수면
        i = 0
        while len(first) < le:
            first.append(s[i])
            i = (i+2)%le
        i = 1
        while len(second) < le:
            second.append(s[i])
            i = (i+2)%le   
            
    else:             #짝수면
        i = 0
        while i < le:
            first.append(s[i])
            i += 2
        i = 1
        while i < le:
            second.append(s[i])
            i += 2
            
    print(''.join(first))
    print(''.join(second))
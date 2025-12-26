import sys
input = sys.stdin.readline

a = int(input())    #시작 온도
b = int(input())    #목표 온도
c = int(input())
d = int(input())
e = int(input())
cnt = 0

if a < 0:        #0도 미만
    cnt += -1 * a * c
    a = 0
if a == 0:       #0도 일때
    cnt += d

tmp = (b - a) * e
cnt += tmp
    
print(cnt)
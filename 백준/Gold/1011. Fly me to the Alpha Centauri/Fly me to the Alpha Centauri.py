import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    dist = y - x
    tmp = cnt = 0
    moving = 0 # 반복 횟수
    
    while tmp < dist:
        cnt += 1
        if cnt % 2:
            moving += 1
        tmp += moving
    print(cnt)
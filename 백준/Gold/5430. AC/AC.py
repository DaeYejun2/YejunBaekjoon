import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    command = input().rstrip()
    n = int(input())
    data = input().rstrip()
    data = data[1:-1].split(',')
    d = deque()
    error = False
    chk = 0
    if n == 0:
        pass
    else:
        for i in data:
            d.append(int(i))
    for i in command:
        if i == 'R':
            chk += 1
        elif i == 'D':
            if d and chk % 2 == 0:
                d.popleft()
            elif d and chk % 2:
                d.pop()
            else:
                error = True
                break
    if error:
        print("error")
    else:
        if chk % 2: d.reverse()
        print('['+','.join(map(str, d))+']')
import sys
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().split())
d = deque([i for i in range(1, n+1)])
chk = 1   #1이 정방향, -1이 방향 바꾼거
cntm = 0
result = []
while d:
    if cntm == m:
        chk *= -1
        cntm = 0
    cnt = 1
    
    if chk == 1:
        while cnt != k:
            cnt += 1
            d.append(d.popleft())
        result.append(d.popleft())
        
    elif chk == -1:
        while cnt != k:
            cnt += 1
            d.appendleft(d.pop())
        result.append(d.pop())
    
    cntm += 1
    
print('\n'.join(map(str, result)))
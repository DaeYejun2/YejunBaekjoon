import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(list(map(int, input().split())))
le = deque()
result = []

for i in range(n):
    le.append((q.popleft(), i+1))

while le:
    tmp, idx = le.popleft()
    result.append(idx)
    
    if tmp > 0:
        le.rotate(-(tmp-1))
    elif tmp < 0:
        le.rotate(-tmp)
        
print(' '.join(map(str, result)))
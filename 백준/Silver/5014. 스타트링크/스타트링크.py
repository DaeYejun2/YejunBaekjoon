import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())# 총f층, 현재위치 s, 목표층 g층, u는 올라가는 버튼, d는 내려가는 버튼
data = [0] * (f+1)
data[s] = 1
move = [u, -d]

q = deque()
q.append(s)
while q:
    if data[g]: print(data[g]-1);exit()
    s = q.popleft()
    for i in range(2):
        x = s+move[i]
        if 0 < x <= f and not data[x]:   #건물 범위에서 벗어나지 않았다면, 방문하지 않았다면
            q.append(x)
            data[x] = data[s] + 1
        
print("use the stairs")
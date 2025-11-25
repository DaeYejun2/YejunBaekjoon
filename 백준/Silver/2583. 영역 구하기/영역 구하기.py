import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = [[0]*m for _ in range(n)]
cnt = 0
result = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(n-y2, n-y1):
        for j in range(x1, x2):
            data[i][j]=1
            
def bfs(x, y):
    q = deque()
    count = 0
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 1:
                count+=1
                data[nx][ny] = 1
                q.append((nx, ny))
    if count == 0: count+=1
    return count

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            result.append((bfs(i, j)))
            cnt += 1
result.sort()  
print(cnt)
print(*result)

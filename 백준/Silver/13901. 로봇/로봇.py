import sys
from collections import deque
input = sys.stdin.readline

q = deque()
r, c = map(int, input().split())
visited = [[-1]*c for _ in range(r)]
k = int(input()) #장애물
for i in range(k):
    a, b = map(int, input().split())
    visited[a][b] = 'x'
    
x, y = map(int, input().split())
q.append((x, y))
visited[x][y] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
data = list(map(int, input().split()))
chk = 1

while chk != 0:
    chk = 0
    for d in data:
        nx = x + dx[d-1]
        ny = y + dy[d-1]
        if 0 <= nx < r and 0 <= ny < c:
            while 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == -1 and visited[nx][ny] != 'x':
                visited[nx][ny] = visited[x][y] + 1
                x = nx; y = ny
                chk += 1
                nx = x + dx[d-1]
                ny = y + dy[d-1]
        
print(x, y)

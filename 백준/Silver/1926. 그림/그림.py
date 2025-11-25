import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]
# 호출이 되면 일단 1개는 잇는거니까 0으로 만들고 tmp를 1로 시작으로 할까

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt_p, cnt_max = 0, [0]

def bfs(x, y):
    tmp = 1
    q = deque()
    q.append((x, y))
    data[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:  #범위 안에 들어 있다면
                q.append((nx, ny))
                data[nx][ny] = 0
                tmp += 1
    cnt_max.append(tmp)
    

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            bfs(i, j)
            cnt_p += 1

print(cnt_p)
print(max(cnt_max))
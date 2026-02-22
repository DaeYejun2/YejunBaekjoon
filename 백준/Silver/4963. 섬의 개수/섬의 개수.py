import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,-1,1,1,-1]

def bfs(x,y):
    q.append((x,y))
    grid[x][y] = 0
    
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                q.append((nx,ny))

while True:
    n,m=map(int,input().split())
    if n == 0 and m == 0: break
    grid = []
    for _ in range(m):
        grid.append(list(map(int,input().split())))

    q = deque()
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                bfs(i,j)
                res += 1
    
    print(res)
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

#적록색약은 빨간색과 초록색 차이를 느끼지 못함
#정상눈이 봤을 때 구역과 적록색약이 봤을 때 구역을 구분해서 출력
#visited 써서 R일때 cnt, G일때 cnt, B일때 cnt 하면 될 듯
data = [input().rstrip() for _ in range(n)]
visited_n = [[0] * n for _ in range(n)]
visited_p = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = [0, 0]

def bfs_n(x, y):
    q_n = deque()
    q_n.append((x, y))
    while q_n:
        x, y = q_n.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited_n[nx][ny]:  #범위 안 벗어나고, 방문하지 않았을 때
                if data[x][y] == data[nx][ny] :      #지금 보고 있는게 다음 항목과 같다면
                    q_n.append((nx,ny))
                    visited_n[nx][ny] = visited_n[x][y] + 1
    result[0] += 1
    
    #적록색약은 빨간색과 초록색 차이를 느끼지 못함
def bfs_p(x, y):
    q_p = deque()
    q_p.append((x, y))
    while q_p:
        x, y = q_p.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited_p[nx][ny]:  #범위 안 벗어나고, 방문하지 않았을 때
                if data[x][y] == data[nx][ny]:
                    q_p.append((nx,ny))
                    visited_p[nx][ny] = visited_p[x][y] + 1
                elif data[x][y] == 'G' and data[nx][ny] == 'R':
                    q_p.append((nx,ny))
                    visited_p[nx][ny] = visited_p[x][y] + 1
                elif data[x][y] == 'R' and data[nx][ny] == 'G':
                    q_p.append((nx,ny))
                    visited_p[nx][ny] = visited_p[x][y] + 1
    result[1] += 1
                    

for i in range(n):
    for j in range(n):
        if not visited_n[i][j]:
            visited_n[i][j] = 1
            bfs_n(i, j)
        if not visited_p[i][j]:
            visited_p[i][j] = 1
            bfs_p(i, j)
            
print(*result)
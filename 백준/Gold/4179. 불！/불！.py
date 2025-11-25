import sys
from collections import deque
input = sys.stdin.readline
#벽과 지훈이, 불 각각의 맵을 따로 제작

n, m = map(int, input().split())
data = []

q_jihun = deque()
q_fire = deque()

visited_j = [[0]*m for _ in range(n)]
visited_f = [[0]*m for _ in range(n)]

for i in range(n):
    tmp = list(input().rstrip())
    for j in range(m):
        if tmp[j] == 'J':
            q_jihun.append((i,j))
            visited_j[i][j] = 1
        elif tmp[j] == 'F':
            q_fire.append((i, j))
            visited_f[i][j] = 1
    data.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 불이 퍼지는 것을 기록할 visited_f와 지훈의 이동을 기록할 visited_j를 따로 만들어 각각을 BFS로 돌아주고 이동거리를 기록
# 2. 특히, 지훈의 이동거리를 기록하는 부분이 중요한데, 
# 불이 이미 퍼지지 않은 곳이거나/ 혹은 불이 도달하는 시간보다 더 짧은 시간안에 지훈이 도달할 수 있다면/ 해당 위치에 대한 값을 기록해주면 된다.
# 3. 그러다가 만약 nx와 ny가 범위를 벗어나게 된다면/ 지훈이 무사히 탈출한 것으로 간주할 수 있으므로 
# x와 y까지의 이동거리를 리턴해주면 답을 구할 수 있다.

def bfs():
    while q_fire:
        x, y = q_fire.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:  #범위에서 벗어나지 않았다면
                if data[nx][ny] != '#' and not visited_f[nx][ny]:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_fire.append((nx,ny))
    while q_jihun:
        x, y = q_jihun.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m :  #범위에서 벗어나지 않았다면
                if data[nx][ny] != '#' and not visited_j[nx][ny]:   # 벽이 아니고, 방문하지 않았다면
                    if not visited_f[nx][ny] or visited_j[x][y] + 1 < visited_f[nx][ny]:  #불도 방문하지 않았거나, 더 빠르다면
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_jihun.append((nx, ny))
            else: #범위에서 벗어났다면 끝
                return visited_j[x][y]
                
    return "IMPOSSIBLE"
          
print(bfs())
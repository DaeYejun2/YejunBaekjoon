import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

water_time = [[-1] * c for _ in range(r)]
hedgehog_time = [[-1] * c for _ in range(r)]

q_water = deque()
q_hedgehog = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 초기 위치 설정
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q_water.append((i, j))
            water_time[i][j] = 0
        elif graph[i][j] == 'S':
            q_hedgehog.append((i, j))
            hedgehog_time[i][j] = 0
        elif graph[i][j] == 'D':
            target_x, target_y = i, j

# 1. 물 BFS: 각 칸에 물이 차는 시간 계산
while q_water:
    x, y = q_water.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            # 빈 공간이면서 아직 물이 차지 않은 곳만
            if graph[nx][ny] == '.' and water_time[nx][ny] == -1:
                water_time[nx][ny] = water_time[x][y] + 1
                q_water.append((nx, ny))

# 2. 고슴도치 BFS: 물보다 빨리 갈 수 있는지 체크하며 이동
while q_hedgehog:
    x, y = q_hedgehog.popleft()
    
    if x == target_x and y == target_y:
        break
        
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            # 돌이 아니고, 아직 방문하지 않은 곳
            if graph[nx][ny] != 'X' and hedgehog_time[nx][ny] == -1:
                # 물이 아예 안 차는 곳이거나, 물보다 먼저 도착할 수 있는 곳
                if water_time[nx][ny] == -1 or hedgehog_time[x][y] + 1 < water_time[nx][ny]:
                    # 비버의 집은 물 시간과 상관없이 갈 수 있으므로 별도 처리 필요 없음 (이미 위 조건에서 걸러짐)
                    hedgehog_time[nx][ny] = hedgehog_time[x][y] + 1
                    q_hedgehog.append((nx, ny))

ans = hedgehog_time[target_x][target_y]
print(ans if ans != -1 else "KAKTUS")
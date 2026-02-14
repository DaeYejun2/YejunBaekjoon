from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

curr_x, curr_y = 0,0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            curr_x, curr_y = i,j
            grid[i][j] = 0
            break

shark_size = 2
eaten_count = 0
total_time = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, size):
    distances = [[-1] * n for _ in range(n)]
    candidate = []
    queue = deque([(x, y)])
    distances[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and distances[nx][ny] == -1:
                if grid[nx][ny] <= size:
                    queue.append((nx,ny))
                    distances[nx][ny] = distances[x][y] + 1
                    if 0 < grid[nx][ny] < size:
                        candidate.append((distances[nx][ny], nx, ny))

    if not candidate: 
        return None
    candidate.sort()
    return candidate[0]


while True:
    result = bfs(curr_x, curr_y, shark_size)

    if result is None: 
        break

    dist, x, y = result
    total_time += dist
    grid[x][y] = 0
    curr_x, curr_y = x, y
    
    eaten_count += 1
    if eaten_count == shark_size:
        eaten_count = 0
        shark_size += 1

print(total_time)
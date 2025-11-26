import sys
from collections import deque
import copy
input = sys.stdin.readline

# n미만 지역은 잠긴다

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]  #임마를 원본 데이터로 쓰고
result = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(tmp, x, y, k):
    q = deque()
    q.append((x, y))
    tmp[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and tmp[nx][ny] >= k:   #범위에서 벗어나지 않았고 영역이 n보다 크거나 같다면
                if tmp[nx][ny] != 0:  # 데이터가 0이 아니면
                    tmp[nx][ny] = 0
                    q.append((nx, ny))
    return 1

for k in range(100):
    cnt = 0
    tmp = copy.deepcopy(data)
    for i in range(n):
        for j in range(n):
            if tmp[i][j] >= k and tmp[i][j] != 0:  #해당 영역이 n보다 크거나 같고, 0이 아니라면 실행
                cnt += bfs(tmp, i, j, k)
    result.append(cnt)
    
print(max(result))
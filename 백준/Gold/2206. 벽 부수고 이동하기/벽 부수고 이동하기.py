import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
#시발 벽을 왜 부셔
for i in range(n):
    data.append(list(map(int, input().rstrip())))
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1   # z: 0은 안부숨, 1은 부숨

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, z):
    q = deque()
    q.append((x,y,z))
    while q:
        a, b, c = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny] == 1 and c == 0:  #다른 이동할 곳이 벽이고 벽파괴를 사용하지 않았다면
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    q.append((nx, ny, 1))
                elif data[nx][ny] == 0 and visited[nx][ny][c] == 0:  #다른 이동할 곳이 벽이 아니고, 벽파괴 할 수 있음
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    q.append((nx,ny,c))                    
    return -1

#벽 부수기를 한번밖에 못쓰는데, 이거는 어떻게 정하냐
#very simple! 0으로 진행하던 애들, 벽을 만난 애들. 이렇게 있으면 어차피 각각이 큐에 담길테니,
#벽을 이미 만나서 부셨으면 이 세계선은 더 이상 벽을 뚫지 못하고
#벽을 아직 만나지 않았다면(4방향으로 나눠서 탐색하니까) 벽을 부술 기회만 남긴채 쭉쭉 가는거다.
#그러다가 종료 조건이 오면, 아무래도 가장 빨리 왔으니까 가장 빠르겠지? 그대로 반환.

print(bfs(0,0,0))
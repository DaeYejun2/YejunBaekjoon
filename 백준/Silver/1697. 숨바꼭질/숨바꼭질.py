import sys
from collections import deque
input = sys.stdin.readline
inf = 100000
n, k = map(int, input().split())

# x-1, x+1, 2*x 각 위치를 queue에 넣고 갈 수 있는 범위를 확인
visited = [0] * (inf + 1)

q = deque()
q.append(n)  # 현재 위치 일단 저장하고
visited[n] = 1

while q:
    if visited[k]: break
    n = q.popleft()
    for i in [n-1, n+1, 2*n]:
        if 0 <= i <= inf and not visited[i]:
            visited[i] = visited[n] + 1
            q.append(i)
            
print(visited[k] - 1)
import sys
from collections import deque
input = sys.stdin.readline
inf = 100000
n, k = map(int, input().split())
visited = [0] * (inf+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 0
    while queue:
        cur = queue.popleft()
        for i in (cur - 1, cur + 1, cur*2):
            if n == k:
                return visited[cur]
            if i == k:
                return visited[cur] + 1
            if 0 <= i <= inf and not visited[i]:
                visited[i] = visited[cur] + 1
                queue.append(i)
                
print(bfs(n))
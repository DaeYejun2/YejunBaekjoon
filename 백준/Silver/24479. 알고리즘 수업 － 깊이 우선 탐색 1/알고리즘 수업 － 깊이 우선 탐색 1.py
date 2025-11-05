import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, v = map(int, input().split())
matrix = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    t, f = map(int, input().split())
    matrix[t].append(f)
    matrix[f].append(t)
for i in range(1, n+1):
    matrix[i].sort()
    
cnt = 1

def dfs(v):
    global cnt
    visited[v] = cnt
    for i in (matrix[v]):
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(v)
for i in range(1, len(visited)):
    print(visited[i])
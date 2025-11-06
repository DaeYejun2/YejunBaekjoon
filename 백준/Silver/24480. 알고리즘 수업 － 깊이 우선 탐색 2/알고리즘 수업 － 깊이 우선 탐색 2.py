import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, v = map(int, input().split())
visited = [0] * (n+1)
matrix = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
for i in range(1, n+1):
    matrix[i].sort(reverse=True)

order = 1

def dfs(v):
    global order
    visited[v] = order
    order += 1

    for i in matrix[v]:
        if visited[i] == 0:
            dfs(i)

dfs(v)

for i in range(1, n+1):
    print(visited[i], end='\n')
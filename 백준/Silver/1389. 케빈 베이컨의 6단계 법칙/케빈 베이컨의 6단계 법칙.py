import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a-=1; b-=1
    graph[a][b] = graph[b][a] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
                
result = 0
bacon = INF
for i in range(n):
    s = sum(graph[i])
    if s < bacon:
        bacon = s
        result = i
        
print(result+1)
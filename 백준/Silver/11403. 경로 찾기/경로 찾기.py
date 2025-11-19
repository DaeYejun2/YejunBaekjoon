import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if max(graph[a][b], graph[a][k]+graph[k][b]) > 1:
                graph[a][b] = 1
            
for i in range(n):
    print(*graph[i])
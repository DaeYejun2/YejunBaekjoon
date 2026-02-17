import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
nxt = [[0]*(n+1) for _ in range(n+1)]

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    v1,v2,c = map(int,input().split())
    if graph[v1][v2] > c:
        graph[v1][v2] = c
        nxt[v1][v2] = v2

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF: 
            graph[i][j] = 0
        print(graph[i][j],end=' ')
    print()

for i in range(1, n+1):
    for j in range(1,n+1):
        if graph[i][j] == 0:
            print(0)
            continue

        path = []
        curr = i
        while curr != 0:
            path.append(curr)
            if curr == j:
                break
            curr = nxt[curr][j]
        
        print(len(path), *path)
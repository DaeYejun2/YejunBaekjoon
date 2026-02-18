import sys
input = sys.stdin.readline

n, m, r = map(int,input().split()) # n: 지역의 개수(노드), m: 가중치 최대 값, r: 간선수
item = []
item=[0]+list(map(int,input().split())) # 각 노드에 있는 아이템 수
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]
res = [[0] for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(r):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1,n+1):
    res[i].append(item[i])
    for j in range(1,n+1):
        if graph[i][j] == INF: graph[i][j] = 0
        if graph[i][j] != 0 and graph[i][j] <= m:
            res[i].append(item[j])
    res[i] = sum(res[i])

max_val = 0
for i in range(1,n+1):
    max_val = max(max_val, res[i])

print(max_val)
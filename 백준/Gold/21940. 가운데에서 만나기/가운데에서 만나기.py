import sys
input = sys.stdin.readline

n,m = map(int,input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)

k = int(input())
city_num = list(map(int,input().split()))

for t in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][t]+graph[t][j])

min_dist = INF
res = []

for x in range(1,n+1):
    max_dist_x = 0
    for c in city_num:
        tmp = graph[c][x] + graph[x][c] # 도시 x를 왕복하는 경우잖아
        max_dist_x = max(max_dist_x, tmp) # 친구들 중 가장 오래걸리는 시간 업데이트

    if max_dist_x < min_dist: # 각 도시의 최악의 왕복 시간 중 가장 짧은 경우
        min_dist = max_dist_x
        res = [x]
    elif max_dist_x == min_dist:
        res.append(x)

res.sort()
print(*res)
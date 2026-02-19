import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())

edges = []
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            weight = edges[j][2]
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node]+weight:
                distance[next_node] = distance[cur_node] + weight
                if i == n-1:
                    return True  # 음수 사이클이 있다
    return False

negatuve_cycle = bf(1)

if negatuve_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF: distance[i] = -1
        print(distance[i])
import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input())

def bf(start,n):
    distance = [INF] * (n+1)
    distance[start] = 0
    for i in range(n):
        for s, e, t in edges:
            if distance[e]>distance[s]+t:
                if i == n-1:
                    return True
                distance[e] = distance[s]+t
    return False

for _ in range(t):
    n,m,w = map(int,input().split())
    edges = []

    for i in range(m):
        s,e,t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))

    for i in range(w):
        s,e,t = map(int,input().split())
        edges.append((s,e,-t))

    negative_cycle = bf(1,n)

    if negative_cycle == True:
        print("YES")
    else: print("NO")
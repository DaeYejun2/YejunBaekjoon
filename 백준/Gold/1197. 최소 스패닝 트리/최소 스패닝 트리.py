import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] < 0: return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())
parent = [-1] * (n+1)
result = 0
cnt = 0

edges = []
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for edge in edges:
    cost, a, b = edge
    x, y = find_parent(parent, a), find_parent(parent, b)
    if  x != y:
        union_find(parent, x, y)
        result += cost
        cnt += 1
        if cnt == n-1: break
        
print(result)
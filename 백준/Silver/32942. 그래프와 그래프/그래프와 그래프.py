import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
graph = [[] for i in range(1, 11)]
for i in range(1, 11):
    for j in range(1, 11):
        if c - a*i == b*j:
             graph[i-1].append(j)
             
for i in range(10):
    if len(graph[i]):
        print(*graph[i])
    else:
        print(0)
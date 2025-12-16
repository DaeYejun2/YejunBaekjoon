import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, group):
    q = deque([start])
    visited[start] = group  #시작 정점 그룹을 설정
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)     #방문하지 않은 정점 추가,
                visited[i] = -1 * visited[x]    #상위 정점과 다른 그룹으로 표현
            elif visited[i] == visited[x]:    #i정점에 방문 했었는데, 상위 그룹과 같은 그룹이라면
                return True                  # True 반환으로 NO 출력
    return False
    

k = int(input())
for i in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (v+1)
    
    for j in range(1, v+1):
        if not visited[j]:
            result = bfs(j, 1)
            if result:
                print("NO")
                break
    else:
        print("YES")
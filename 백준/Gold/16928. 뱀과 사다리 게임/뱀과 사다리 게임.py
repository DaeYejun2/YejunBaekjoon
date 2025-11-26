import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())  #n은 사다리, m은 뱀
q = deque()
sadari = []; baaam = []
visited = [False for _ in range(101)]
for i in range(n):
    sadari.append([int(x) for x in input().rstrip().split()])
for i in range(m):
    baaam.append([int(x) for x in input().rstrip().split()])

def bfs():
    q = deque()
    q.append((1, 0))  # 시작 지점, 방문 횟수
    visited[1] = True
    while q:
        x, cnt = q.popleft()
        if x == 100:
            print(cnt)
            break
        for i in range(1, 7):
            nx = x + i
            if nx > 100: continue
            
            for k in range(len(sadari)):
                if nx == sadari[k][0] and not visited[nx]: #사다리 출발 지점을 만났고, nx가 방문하지 않았으면
                    visited[nx] = True
                    q.append((sadari[k][1], cnt+1)) #끝지점과 cnt만 +1 해서 엔큐
            for j in range(len(baaam)):
                if nx == baaam[j][0] and not visited[nx]:
                    visited[nx] = True
                    q.append((baaam[j][1], cnt+1))
            
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, cnt+1))
            

bfs()
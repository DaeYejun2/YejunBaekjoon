import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    visited = [False] * 10001
    a,b=map(int,input().split())
    visited[a] = True
    q = deque([(a,'')])
    
    while q:
        curr, dslr = q.popleft()

        if curr == b:
            break

        # D
        nxt = (curr*2) % 10000
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, dslr+'D'))
        
        # S
        nxt = (curr-1) % 10000
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, dslr+'S'))

        # L - 좌측으로 회전
        nxt = (curr) % 1000 * 10 + (curr//1000)
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, dslr+'L'))

        # R - 우측으로 회전
        nxt = (curr%10) * 1000 + (curr//10)
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, dslr+'R'))

    print(dslr)
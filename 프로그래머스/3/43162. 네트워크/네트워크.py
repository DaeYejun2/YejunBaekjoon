from collections import deque

def solution(n, computers):
    visited = [False]*n
    res = 0
    
    for i in range(n):
        if not visited[i]:
            res += 1
            queue = deque([i])
            visited[i] = True
            
            while queue:
                curr = queue.popleft()
                for j in range(n):
                    if computers[curr][j] == 1 and not visited[j]:
                        visited[j] = True
                        queue.append(j)
    return res
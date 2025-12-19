import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
l = []
visited = [0]*n

def backtracking(start):
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(start, n):
        if visited[i] == 0 and data[i] not in l:
            l.append(data[i])
            visited[i] = 1
            backtracking(i+1)
            l.pop()
            visited[i] = 0
            
backtracking(0)
import sys
input = sys.stdin.readline
#중복 순열

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
l = []
visited = [0] * n

def backtracking():
    check = 0
    if len(l) == m:
        print(*l)
        return 
    
    for i in range(n):
        if check != data[i] and visited[i] == 0:
            l.append(data[i])
            visited[i] = 1
            check = data[i]
            backtracking()
            l.pop()
            visited[i] = 0
        
backtracking()
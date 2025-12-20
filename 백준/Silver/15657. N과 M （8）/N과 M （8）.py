import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
l = []

def backtracking(start):
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(start, n):
        l.append(data[i])
        backtracking(i)
        l.pop()

backtracking(0)
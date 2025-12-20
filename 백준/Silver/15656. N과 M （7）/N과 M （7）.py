import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
l = []

def backtracking():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(n):
        l.append(data[i])
        backtracking()
        l.pop()

backtracking()
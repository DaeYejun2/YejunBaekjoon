import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
l = []

def backtracking():
    check = 0
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(n):
        if check != data[i]:
            check = data[i]
            l.append(data[i])
            backtracking()
            l.pop()
    
backtracking()
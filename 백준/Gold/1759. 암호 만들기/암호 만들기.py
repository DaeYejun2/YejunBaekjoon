import sys
input = sys.stdin.readline

l, c = map(int, input().split())
data = sorted(list(map(str, input().strip().split())))
le = []

def backtracking(start):
    if len(le) == l:
        cnt = 0
        for j in ['a', 'e', 'i', 'o', 'u']:
            if j in le: cnt += 1
        if cnt >= 1 and cnt <= l-2:
            print(''.join(map(str, le)))
        return
    
    for i in range(start, c):
        if data[i] not in le:
            le.append(data[i])
            backtracking(i+1)
            le.pop()
        
backtracking(0)
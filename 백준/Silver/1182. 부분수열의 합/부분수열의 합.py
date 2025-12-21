import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0

def backtracking(cur, tot):
    global cnt
    if cur == n:
        if tot == s:
            cnt += 1
        return
    
    backtracking(cur + 1, tot+data[cur]) #현재 원소를 포함하는 경우
    backtracking(cur + 1, tot)           #현재 원소를 포함하지 않는 경우

backtracking(0, 0)
if s == 0: cnt -= 1
print(cnt)
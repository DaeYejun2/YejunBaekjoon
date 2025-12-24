import sys
input = sys.stdin.readline

n = int(input())
cup = [1, 0, 0]
ans = 0

for i in range(n):
    a, b = map(int, input().split())
    cup[a-1], cup[b-1] = cup[b-1], cup[a-1]
    
for i in range(3):
    if cup[i] == 1: ans = i+1
if ans == 0: print(-1)
else: print(ans)
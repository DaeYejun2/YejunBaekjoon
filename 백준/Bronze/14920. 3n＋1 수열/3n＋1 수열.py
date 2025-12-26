import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
while True:
    if n == 1:
        break
    if n % 2:
        n = 3*n + 1
        cnt += 1
    else:
        n = n // 2
        cnt += 1
    if n == 1:
        break
    
print(cnt+1)
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

while True:
        if n >= 5 and n % 5 == 0:
            cnt += n // 5
            n %= 5
        else:
            n -= 2
            cnt += 1
        if n < 2: break
            
if n == 0: print(cnt)
else: print(-1)
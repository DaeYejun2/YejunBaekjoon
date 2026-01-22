import sys
input = sys.stdin.readline

n = int(input())
coin = [500, 100, 50, 10, 5, 1]
n = 1000-n
ans = 0
for c in coin:
    ans += n // c
    n %= c

print(ans)
import sys
input = sys.stdin.readline

def solve(n):
    prime_cnt = []
    for p in range(2, n+1):
        cnt = 0
        while n % p == 0:
            cnt += 1
            n //= p
        if cnt:
            prime_cnt.append([p, cnt])
    for p in prime_cnt:
        print(*p)

t = int(input())
for _ in range(t):
    solve(int(input()))
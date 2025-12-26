import sys
input = sys.stdin.readline

n = int(input())
ans = 0

while True:
    tmp = 1
    if n < 10:
        break
    while n != 0:
        tmp = tmp * (n % 10)
        n //= 10
    ans += 1
    
    n = tmp
    
print(ans)
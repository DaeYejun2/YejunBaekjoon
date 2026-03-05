import sys
input = sys.stdin.readline

n = 1299710
prime = [True]*n
prime[0]=prime[1] = False

for i in range(2, int((n**0.5))+1):
    for j in range(i*i, n, i):
        prime[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    if prime[n]: print(0)
    else:
        tmp = n
        cnt = 0
        while not prime[tmp]:
            cnt += 1
            tmp -= 1
        tmp = n
        while not prime[tmp]:
            cnt += 1
            tmp += 1
        print(cnt)
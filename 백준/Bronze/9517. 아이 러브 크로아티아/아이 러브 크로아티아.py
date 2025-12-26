import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
tmp = 0

for i in range(n):
    data = list(map(str, input().strip().split()))
    tmp += int(data[0])
    if tmp > 210:
        ans = k
    elif data[1] == 'T':
        k += 1
        if k == 9: k = 1
        
print(ans)
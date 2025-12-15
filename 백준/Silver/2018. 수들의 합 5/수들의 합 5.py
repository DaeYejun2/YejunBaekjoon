import sys
input = sys.stdin.readline

n = int(input())

end = 0
cnt = 0
tmp = 0

for start in range(n):
    while tmp < n and end < n:
        tmp += end + 1
        end += 1
    if tmp == n:
        cnt += 1
    tmp -= start + 1
    
print(cnt)
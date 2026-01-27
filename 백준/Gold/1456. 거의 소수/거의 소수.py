import sys
input = sys.stdin.readline

a, b = map(int, input().split())
end = int(b**0.5)
arr = [i for i in range(end+1)]; arr[1] = 0

for i in range(2, end+1):
    if arr[i] == 0: continue
    for j in range(i*i, end+1, i):
        arr[j] = 0

cnt = 0
for i in range(2, end+1):
    if arr[i] != 0:
        tmp = i
        while tmp <= b/i:
            tmp *= i
            if tmp >= a: cnt += 1

print(cnt)
import sys
input = sys.stdin.readline

arr = [i for i in range(123456*2 + 1)]; arr[1] = 0
end = int((123456*2)**0.5)

for i in range(2, end+1):
    if arr[i] == 0: continue
    for j in range(i*i, 123456*2+1, i):
        arr[j] = 0

n = int(input())
while  n != 0:
    cnt = 0
    for i in range(n+1, 2*n+1):
        if arr[i] != 0: cnt += 1
    print(cnt)
    n = int(input())
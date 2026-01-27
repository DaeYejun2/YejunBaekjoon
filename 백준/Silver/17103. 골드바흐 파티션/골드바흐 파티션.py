import sys
input = sys.stdin.readline

t = int(input())
data = []
for _ in range(t):
    data.append(int(input()))

m = max(data)
arr = [i for i in range(m+1)]; arr[1] = 0
end = int(m**0.5)

for i in range(2, end+1):
    if arr[i] == 0: continue
    for j in range(i*i, m+1, i):
        arr[j] = 0

for d in data:
    cnt = 0
    for i in arr[:d]:
        if i != 0:
            tmp = d - i
            if tmp < 0 or i > tmp: break
            if arr[tmp]:
                cnt += 1
    
    print(cnt)
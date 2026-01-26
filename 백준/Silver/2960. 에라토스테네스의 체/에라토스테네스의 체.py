import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(n+1)]; arr[1] = 0
idx = [0]*(n+1)
l = 0

for i in range(2, n+1):
    if arr[i] == 0: continue
    else:
        if i not in idx:
            idx[l] = i
            l+=1
        for j in range(i*i, n+1, i):
            arr[j] = 0
            if j not in idx:
                idx[l] = j
                l+=1

print(idx[k-1])
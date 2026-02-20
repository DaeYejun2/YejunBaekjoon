import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
s = int(input())

for i in range(n):
    if s <= 0:
        break
    
    max_val = arr[i]
    max_idx = i
    
    for j in range(i + 1, min(n, i + s + 1)):
        if arr[j] > max_val:
            max_val = arr[j]
            max_idx = j
            
    for k in range(max_idx, i, -1):
        arr[k], arr[k-1] = arr[k-1], arr[k]
        s -= 1
        
print(*arr)
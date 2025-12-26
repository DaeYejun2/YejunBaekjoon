import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = []; B = []
match = [0]*n

for i in range(n):
    A.append(int(input()))
    
for i in range(m):
    B.append(int(input()))
    
for i in range(m):
    for j in range(n):
        if B[i] >= A[j]:
            match[j] += 1
            break
            
max_ = max_idx = 0
for i in range(n):
    if max_ < match[i]:
        max_ = match[i]; max_idx = i
        
print(max_idx + 1)
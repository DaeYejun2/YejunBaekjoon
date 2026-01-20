import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n): data.append(int(input()))
data = data[::-1]
ans = 0; 
for i in range(n-1):
    cnt = 0
    while data[i] <= data[i+1]:
        cnt += 1
        data[i+1] -= 1
    ans += cnt
    
print(ans)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split(',')))

for i in range(k):
    for j in range(n-1):
            data[j] = data[j+1]-data[j]
        
print(','.join(map(str, data[:n-k])))
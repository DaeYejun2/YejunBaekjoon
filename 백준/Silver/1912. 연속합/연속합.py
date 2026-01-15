import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
max_val = data[0]
current = data[0]

for i in range(1, n):
    current = max(data[i], current+data[i])
    max_val = max(current, max_val)
    
print(max_val)
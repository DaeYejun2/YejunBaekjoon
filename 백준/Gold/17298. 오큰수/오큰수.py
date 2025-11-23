import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
arr = [-1]*n
stack = []

for i in range(n):
    while stack and data[i] > data[stack[-1]]:
        arr[stack.pop()] = data[i]
        
    stack.append(i)
    
print(*arr)
import sys
input = sys.stdin.readline
n = int(input())
data = []
stack = []
for i in range(n-1):
    data.append(int(input()))
d = int(input())
    
while data:
    if stack and data[-1] > stack[-1]:
        stack.append(data.pop())
    elif not stack and d < data[-1]:
        stack.append(data.pop())
    else: data.pop()
    
print(len(stack)+1)
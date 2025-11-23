import sys
input = sys.stdin.readline

data = []
stack = []
n = int(input())
for i in range(n):
    data.append(int(input()))
result = 0

for x in data:
    while stack and x >= stack[-1]:
        stack.pop()
       
    result += len(stack) 
    stack.append(x)
    
print(result)
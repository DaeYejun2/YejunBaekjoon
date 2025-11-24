import sys
input = sys.stdin.readline

cnt = 0
t = int(input())

for i in range(t):
    data = input().rstrip()
    stack = []  #일치하면 빼는 방식으로 ㄱㄱ
    for x in data:
        if stack:
            if x == stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)
            
    if not stack:
        cnt += 1
        
print(cnt)
import sys
input = sys.stdin.readline

#백스페이스: -(커서 앞에 글자가 있다면), <, >는 커서의 움직임(움직일 수 있다면), 
t = int(input())
stack = [] #본체
tmp = [] #서브

for i in range(t):
    data = input().rstrip()
    stack = []
    for x in data:
        if x == '<':
            if stack:
                tmp.append(stack.pop())
        elif x == '>':
            if tmp:
                stack.append(tmp.pop())
        elif x == '-':
            if stack:
                stack.pop()
        else:
            stack.append(x)
    while tmp:
        stack.append(tmp.pop())
    for i in range(len(stack)):
        print(stack[i], end='')
    print()
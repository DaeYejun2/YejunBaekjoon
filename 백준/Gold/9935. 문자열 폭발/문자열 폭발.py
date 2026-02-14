data = input()
s = input()
le = len(s)
stack = []

for d in data:
    stack.append(d)
    if len(stack) >= le:
        tmp = ''
        for i in range(-le, 0):
            tmp += stack[i]
        if s == tmp:
            for i in range(le):
                stack.pop()
    
if len(stack):
    print(''.join(stack))
else:
    print('FRULA')
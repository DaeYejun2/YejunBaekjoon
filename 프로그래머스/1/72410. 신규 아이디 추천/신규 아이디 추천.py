def solution(new_id):
    stack = []

    for n in new_id:
        if len(stack) == 15: break
        if ord('a') <= ord(n) <= ord('z') or ord('A') <= ord(n) <= ord('Z'):
            stack.append(n)
        elif n == '-' or n =='_' or n =='.':
            if stack:
                if stack[-1] == '.' and n == '.':
                    continue
                else:
                    stack.append(n)
            else:
                if n =='.': continue
                else:
                    stack.append(n)
        elif 48 <= ord(n) <= 57:
            stack.append(n)
        
        
    if len(stack) == 0: stack.append("a")    
    if stack[-1] == '.': stack.pop()
    while len(stack) < 3:
        stack.append(stack[-1])

    res = ''.join(stack)
    res = res.lower()
    return res
def solution(arr):
    stack = []
    for a in arr:
        if stack:
            if stack[-1] != a: stack.append(a)
        else: stack.append(a)
    return stack
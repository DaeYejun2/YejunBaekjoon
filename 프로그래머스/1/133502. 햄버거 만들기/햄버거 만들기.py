def solution(ingre):
    # 1: 빵, 2: 야채, 3: 고기
    stack = []
    cnt = 0
    for i in ingre:
        stack.append(i)
        if len(stack) >= 4:
            if stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3 and stack[-1] == 1:
                for _ in range(4):stack.pop()
                cnt += 1
    return cnt
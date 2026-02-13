from collections import deque

def solution(dart):
    res = deque()
    tmp = deque()
    ans = []
    i = 0
    while i < len(dart):
        if ord('0') <= ord(dart[i]) <= ord('9'):
            if i + 1 < len(dart):
                if dart[i+1] == '0':
                    res.append(10)
                    i += 2
                    continue
            res.append(int(dart[i]))
        else:
            tmp.append(dart[i])
            if i + 1 < len(dart):
                if dart[i+1] == '*' or dart[i+1] == '#':
                    tmp.append(dart[i+1])
                    i+=1

        i+=1

    i = 0
    while tmp:
        if tmp[0] == 'S':
            ans.append(res.popleft())
            tmp.popleft()
        elif tmp[0] == 'D':
            ans.append((res.popleft())**2)
            tmp.popleft()
        elif tmp[0] == 'T':
            ans.append((res.popleft())**3)
            tmp.popleft()
        elif tmp[0] == '*':
            if len(ans) > 1:
                ans[-2] *= 2
            ans[-1] *= 2
            tmp.popleft()
        else:
            ans[-1] *= -1
            tmp.popleft()
        
    return (sum(ans))
def s(num):
    tmp = 0
    for i in range(1, num+1):
        if num % i == 0: tmp += 1
    return tmp

def solution(left, right):
    res = 0
    for j in range(left, right+1):
        if s(j) % 2: res -=j
        else: res+=j
    return res
def solution(x):
    s = 0 # 자릿수의 합
    for l in list(str(x)): 
        s += int(l)
    if int(x) % s == 0: return True
    return False
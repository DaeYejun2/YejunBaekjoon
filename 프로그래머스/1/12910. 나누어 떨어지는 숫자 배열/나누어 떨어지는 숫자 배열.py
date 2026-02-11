def solution(arr, divisor):
    arr.sort()
    res = []
    chk = 0
    for a in arr:
        if a % divisor == 0:
            res.append(a)
            chk+=1
    if chk == 0: return [-1]
    return res
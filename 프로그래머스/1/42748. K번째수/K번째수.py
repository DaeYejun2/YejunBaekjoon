def solution(array, commands):
    res = []
    for i, j, k in commands:
        tmp = array[i-1:j]
        tmp.sort()
        res.append(tmp[k-1])
        
    return res
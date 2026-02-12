def solution(name, yearning, photo):
    dic = {}
    for n, y in zip(name, yearning):
        dic[n] = y
    
    res = [[] for i in range(len(photo))]

    for i, pho in enumerate(photo):
        for p in pho:
            if p in dic:
                res[i].append(dic[p])
        res[i] = sum(res[i])
    return res
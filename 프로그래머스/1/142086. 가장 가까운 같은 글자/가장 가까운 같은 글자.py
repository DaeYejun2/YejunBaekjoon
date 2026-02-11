def solution(s):
    dic = {}
    res = []
    for i, se in enumerate(s):
        if se in dic:
            res.append(i-dic[se])
        else:
            res.append(-1)
        dic[se] = i
            
    return res
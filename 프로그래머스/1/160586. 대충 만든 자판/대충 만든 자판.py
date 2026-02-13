def solution(keymap, targets):
    dic = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k not in dic:
                dic[k] = i+1
            else:
                dic[k] = min(dic[k], i+1)
    
    res = []
    for tar in targets:
        tmp = 0
        for t in tar:
            if t in dic:
                tmp += dic[t]
            else: 
                tmp = -1
                break
        res.append(tmp)
    return res
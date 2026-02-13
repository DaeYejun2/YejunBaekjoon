def solution(X, Y):
    dic_x = {}
    dic_y = {}
    res = ''
    for x in X:
        if x not in dic_x:
            dic_x[x] = 1
        else: dic_x[x] += 1
    for y in Y:
        if y not in dic_y:
            dic_y[y] = 1
        else: dic_y[y] += 1
    
    dic_x = dict(sorted(dic_x.items(), reverse=True))
    dic_y = dict(sorted(dic_y.items(), reverse=True))
    
    if len(dic_x) < len(dic_y):
        for x in dic_x:
            if x in dic_y:
                tmp = min(dic_x[x], dic_y[x])
                res += x*tmp
    else:
        for x in dic_y:
            if x in dic_x:
                tmp = min(dic_x[x], dic_y[x])
                res += x*tmp
                
    if res >= '1': return res
    elif res >= '0': return "0"
    else: return "-1"
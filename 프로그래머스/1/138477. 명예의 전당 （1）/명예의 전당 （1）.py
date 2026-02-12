def solution(k, score):
    res = []
    tmp = []
    for i, s in enumerate(score):
        if i == 0:
            res.append(s)
            tmp.append(s)
        elif i < k:
            tmp.append(s)
            res.append(min(tmp))
            print(tmp)
            if i == k-1: tmp.sort(reverse=True)
        else:
            if s > tmp[-1]:
                tmp.pop()
                tmp.append(s)
                tmp.sort(reverse=True)
                print(tmp)
            res.append(tmp[-1])
            
            
    return res
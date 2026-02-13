def solution(data, ext, val_ext, sort_by):
    dic = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    res = []
    for d in data:
        if int(d[dic[ext]]) < val_ext:
            res.append(d)

    res.sort(key=lambda x: x[dic[sort_by]])
    return res
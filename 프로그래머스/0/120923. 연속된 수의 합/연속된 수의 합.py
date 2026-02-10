def solution(num, total):
    tmp = total
    cnt = 0
    while True:
        tmp = total - cnt
        res = []
        for i in range(num):
            res.append(tmp)
            tmp -= 1
        if sum(res) == total: 
            res.sort()
            return res
        if sum(res) < total: cnt -= 1
        else: cnt += 1
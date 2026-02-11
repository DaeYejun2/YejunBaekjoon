def solution(d, budget):
    res = len(d)
    d.sort()
    while sum(d) > budget:
        res -= 1
        d.pop()
    return res
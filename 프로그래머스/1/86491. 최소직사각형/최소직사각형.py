def solution(sizes):
    for s in sizes:
        s.sort()
    w = []
    h = []
    for s in sizes:
        w.append(s[0])
        h.append(s[1])
    
    return max(w) * max(h)
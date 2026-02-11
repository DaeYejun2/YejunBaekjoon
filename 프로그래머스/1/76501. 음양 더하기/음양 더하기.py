def solution(absolutes, signs):
    res = 0
    idx = 0
    for s in signs:
        if s: res+=absolutes[idx]
        else: res-=absolutes[idx]
        idx+=1
    return res
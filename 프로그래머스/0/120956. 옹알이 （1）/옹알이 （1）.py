def solution(babbling):
    res = 0
    
    for b in babbling:
        for i in ["aya", "ye", "woo", "ma"]:
            b = b.replace(i, " ")
        if b.strip()=="": res += 1
    return res
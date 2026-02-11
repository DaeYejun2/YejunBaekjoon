def solution(s):
    s=s.upper()
    count_p = s.count("P")
    count_y = s.count("Y")
    if count_p == count_y: return True
    return False
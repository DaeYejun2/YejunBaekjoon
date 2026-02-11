def solution(n):
    s = "수박" * (n//2)
    if n%2: return s + "수"
    return s
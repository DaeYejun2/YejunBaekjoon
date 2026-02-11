def solution(n):
    tmp = int(n**0.5)
    if n == tmp**2: return (tmp+1)**2
    return -1
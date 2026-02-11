def solution(n):
    l = [int(i) for i in list(str(n))]
    l.sort(reverse=True)
    l = ''.join(map(str, l))
    return int(l)
    
print(solution(118372))
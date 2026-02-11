def solution(n):
    answer = list(str(n))
    res = []
    for i in answer[::-1]:
        res.append(int(i))
    return res
    
print(solution(12345))
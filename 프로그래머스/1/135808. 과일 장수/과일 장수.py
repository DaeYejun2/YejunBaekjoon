def solution(k, m, score):
    score.sort(reverse=True)
    res = 0

    for i in range(0, len(score)-m+1, m):
        res += min(score[i:i+m]) * m
        
    return res
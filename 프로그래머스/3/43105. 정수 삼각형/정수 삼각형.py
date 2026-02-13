def solution(tri):
    for i in range(len(tri)-1, 0, -1): # 4부터 0까지
        for j in range(len(tri[i])-1):  # 0 부터 tri[i]까지
            tri[i-1][j] += max(tri[i][j],tri[i][j+1])
    return (tri[0][0])
    
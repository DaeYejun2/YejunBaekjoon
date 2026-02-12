def solution(n):
    data = [True] * (n+1)
    data[0]=data[1]=False
    for i in range(2, int(n**0.5)+1):
        for j in range(i*i, n+1, i):
            data[j]=False
    return data.count(True)
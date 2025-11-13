import sys
input = sys.stdin.readline

#n이 1, 2, 3인 경우를 우선 저장, 1빼기, 2나누기, 3나누기 각 경우를 해서 최소값을 배열에 저장

n = int(input())

def dp(n):
    d = [0]*(n+1)
    if n >= 2: d[2] = 1
    if n >= 3: d[3] = 1
    
    for i in range(4, n+1):
        if i % 3 == 0 and i % 2 == 0:
            d[i] = min(d[i-1], d[i//3], d[i//2]) + 1
        elif i % 3 == 0:
            d[i] = min(d[i-1], d[i//3]) + 1
        elif i % 2 == 0:
            d[i] = min(d[i-1], d[i//2]) + 1
        else:
            d[i] = d[i-1] + 1
        
    print(d[n])
    
dp(n)
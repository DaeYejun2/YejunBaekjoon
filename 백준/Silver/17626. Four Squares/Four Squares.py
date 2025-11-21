import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    _min=int(1e9)
    for j in range(1,int(i**0.5)+1): # i보다 작은 제곱수(j**2)를 뺌
        _min = min(_min, dp[i-j**2]) # 'i-j**2'인 경우의 최소 제곱수의 개수
    dp[i]=_min+1
    
print(dp[n])
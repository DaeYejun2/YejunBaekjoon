import sys
input = sys.stdin.readline

n=int(input()) # 계단 개수
s=[int(input()) for _ in range(n)] # 계단 리스트
dp=[0]*(n) # dp 리스트

if len(s)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[1] + s[0]  #2까진 값이 바뀌는 경우의 수가 1가지
    for i in range(2, n):
        #직전칸에서 올라온 경우, 전전칸에서 올라온 경우 들의 최댓값
        dp[i] = max(dp[i-3] + s[i-1], dp[i-2]) + s[i]
    
    print(dp[-1])
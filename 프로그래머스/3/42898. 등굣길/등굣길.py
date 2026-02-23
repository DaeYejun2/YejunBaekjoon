def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: continue 
            if [j,i] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:
                dp[i][j] = 0
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
                
    return (dp[n][m])
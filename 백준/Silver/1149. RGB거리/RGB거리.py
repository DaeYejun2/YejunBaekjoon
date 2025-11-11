import sys
input = sys.stdin.readline

n = int(input())
rgb = []
dp = []
dp = [[0] * 3 for _ in range(n)]
for i in range(n):
    rgb.append(list(map(int, input().split())))
dp[0] = rgb[0]

for i in range(1, n): 
    #0은 빨강, 1은 초록, 2는 파랑.
    # i-1번째. 즉, 색 다른 바로 위 요소들 중 가장 작과 원래 값과 합해서 저장.
    #위에서 부터 차근차근 하니까 계속 최소 값이 저장될 것.
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
    
print(min(dp[n-1]))
#include <string>
#include <vector>

using namespace std;
const int MOD = 1000000007;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
    
    for(const auto& p: puddles)
        dp[p[1]][p[0]] = -1;
    
    dp[1][1] = 1;
    
    for(int y = 1; y <= n; y++)
        for(int x = 1; x <= m; x++){
            if(y==1&&x==1 || dp[y][x] == -1) continue;
            
            // 위->아래 
            if(dp[y-1][x] != -1)
                dp[y][x] = (dp[y-1][x] + dp[y][x]) % MOD;
            // 왼->오
            if(dp[y][x-1] != -1)
                dp[y][x] = (dp[y][x-1] + dp[y][x]) % MOD;
        }

    
    return dp[n][m];
}
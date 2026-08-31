#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int solution(int N, int number) {
    int answer = 0;
    
    // dp[k]는 N을 정확히 k개 써서 만들 수 있는 숫자들의 모음.
    vector<unordered_set<int>> dp(9);  
    
    // 1. 이어 붙인 수 미리 생성 (5, 55, 555, ...)
    int base = 0;
    for(int k = 1; k <= 8; k++){
        base = base * 10 + N;
        dp[k].insert(base);
    }
    
    // 2. DP 진행
    for(int k = 1; k <= 8; k++){
        for(int i = 1; i < k; i++){
            int j = k - i;  // i개를 사용한 결과와 j개 사용한 결과를 조합
            // i, j 두 덩어리의 합은 k여야 하므로 i+j=k -> j=k-i
            
            for(int a: dp[i]){
                for(int b: dp[j]){
                    dp[k].insert(a+b);
                    dp[k].insert(a-b);
                    dp[k].insert(a*b);
                    if(b != 0) dp[k].insert(a/b);
                }
            }
        }
        if(dp[k].count(number)) return k;
    }
    return -1;
}


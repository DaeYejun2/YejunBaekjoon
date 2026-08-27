#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    sort(dungeons.begin(), dungeons.end());
    
    do{
        int cur_k = k;
        int count = 0;
        for(int i = 0; i < dungeons.size(); i++){
            if (cur_k >= dungeons[i][0]){
                cur_k -= dungeons[i][1];
                count++;
            }
            else break;
        }
        answer = max(answer, count);
    }while(next_permutation(dungeons.begin(), dungeons.end()));
    
    
    return answer;
}
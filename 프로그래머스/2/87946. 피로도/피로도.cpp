#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    sort(dungeons.begin(), dungeons.end());
    
    do{
        int cur_k = k;
        int tmp = 0;
        for(int i = 0; i < dungeons.size(); i++){
            if(cur_k>=dungeons[i][0]){
                cur_k -=dungeons[i][1];
                tmp++;
            }
            else break;
        }
        answer = max(answer, tmp);
        
    }while(next_permutation(dungeons.begin(), dungeons.end()));
    
    
    
    
    
    
    return answer;
}
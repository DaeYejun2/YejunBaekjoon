#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<double, int>> fail_rates;
    sort(stages.begin(), stages.end());  // 1, 2, 2, 2, 3, 3, 4, 5
    
    int tot_users = stages.size();  // 각 스테이지별 도전자
    int idx = 0;                    // stage 순회용
    
    for(int cur_stage = 1; cur_stage <= N; cur_stage++){
        int tmp = 0;
        while(idx < stages.size() && cur_stage == stages[idx]){
            tmp++;
            idx++;
        }
        
        double rate = 0.0;
        
        if (tot_users > 0) rate = (double) tmp / tot_users;
        fail_rates.push_back({rate, cur_stage});
             
        tot_users -= tmp;
    }
    
    sort(fail_rates.begin(), fail_rates.end(), [](auto& a, auto& b){
        if(a.first == b.first) return a.second < b.second;
        return a.first > b.first;
    });
    
    for(auto& a: fail_rates) answer.push_back(a.second);
    
    return answer;
}
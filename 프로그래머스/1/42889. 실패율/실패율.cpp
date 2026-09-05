#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<double, int>> fail_rates;
    sort(stages.begin(), stages.end());
    // 실패율을 구하고 그 인덱스 값으로. 실패율이 높은 순으로
    int total_users = stages.size();
    int idx = 0;

    for(int cur_stage = 1; cur_stage <= N; cur_stage++){
        int cnt = 0;
        
        while(idx < stages.size() && stages[idx] == cur_stage){
            cnt++;
            idx++;
        }
        
        // 스테이지에 도달한 유저가 없으면 실패율 0
        double rate = 0.0;
        
        if(total_users > 0) rate = (double)cnt / total_users;
        fail_rates.push_back({rate, cur_stage});
        
        // 다음 스테이지 도달 인원은 현재 스테이지 실패자만큼 감소
        total_users -= cnt;
    }
    
    sort(fail_rates.begin(), fail_rates.end(),[](const pair<double, int>& a, const pair<double, int>&b){
        if(a.first == b.first) return a.second < b.second;
        return a.first > b.first;
    });
    
    for(const auto& p: fail_rates) answer.push_back(p.second);
    
    
    
    return answer;
}
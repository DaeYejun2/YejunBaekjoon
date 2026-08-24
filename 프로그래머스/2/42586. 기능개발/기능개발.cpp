#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int max_day = 0;
    
    for(int i = 0; i < progresses.size(); i++){
        int remain = 100 - progresses[i];
        int days = (remain % speeds[i] == 0) ? (remain/speeds[i]) : (remain/speeds[i]+1);
        
        if(answer.empty() || days > max_day){
            answer.push_back(1);
            max_day = days;
        }
        else answer.back()++;
    }
    return answer;
}
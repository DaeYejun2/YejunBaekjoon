#include <string>
#include <vector>
#include <deque>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    deque<int> q;
    
    for (int p: prices) q.push_back(p);
    
    while(!q.empty()){
        int cur = q.front();
        q.pop_front();
        
        int sec = 0;
        for(int i = 0; i < q.size(); i++){
            sec++;
            
            if (cur > q[i]) break;
        }
        answer.push_back(sec);
    }
    
    return answer;
}
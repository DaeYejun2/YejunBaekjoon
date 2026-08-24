#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    queue<pair<int, int>> q;    // {우선순위(priorities), 원래 인덱스}
    priority_queue<int> pq;     // 우선순위 정렬(최댓값 추적)
    
    for (int i = 0; i < priorities.size(); i++){
        q.push({priorities[i], i});
        pq.push(priorities[i]);
    }
    int cnt = 0;
    while(!q.empty()){
        auto[p, idx] = q.front();
        q.pop();
        
        if (p == pq.top()){
            cnt++;
            pq.pop();
            if (idx == location) return cnt;
        }
        else q.push({p, idx});
    }
    return cnt;
}
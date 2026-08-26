#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int,vector<int>,greater<int>> pq;
    
    for(int s: scoville) pq.push(s);
    int cnt = 0;
    while(!pq.empty() && pq.top() < K){
        if(cnt > scoville.size()) return -1;
        int x = pq.top();
        pq.pop();
        if(pq.empty()) return -1;
        int tmp = pq.top();
        pq.pop();
        tmp = tmp*2 + x;
        pq.push(tmp);
        cnt++;
    }    
    
    return cnt;
}
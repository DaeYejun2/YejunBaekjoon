#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int,vector<int>,greater<int>> pq;
    
    for(int s: scoville) pq.push(s);
    int cnt = 0;
    
    while(pq.size() >= 2 && pq.top() < K){
        int x = pq.top();
        pq.pop();
        
        int tmp = pq.top();
        pq.pop();
        
        pq.push(tmp*2 + x);
        cnt++;
    }    
    
    return (pq.top() < K) ? -1 : cnt;
}

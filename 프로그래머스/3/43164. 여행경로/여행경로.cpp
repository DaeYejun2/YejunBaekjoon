#include <string>
#include <vector>
#include <algorithm>

using namespace std;
vector<string> answer;

// bool을 반환하여 정답 경로를 찾으면 즉시 모든 재귀를 탈출
bool dfs(vector<vector<string>>& tickets, string cur, vector<bool>& visited, int count){
    answer.push_back(cur);
    
    if(count == tickets.size()) {
        return true;
    }
    
    for(int i = 0; i < tickets.size(); i++){
        if(!visited[i] && tickets[i][0] == cur){
            visited[i] = true;
            
            // 다음 반복에서 끝까지 도달했다면(true 반환)원복하지 않고 true 반환
            if (dfs(tickets, tickets[i][1], visited, count+1)) return true;
            
            // 막다른 길에 도달한 경우 상태 원복
            visited[i] = false;
        }
    }
    // 이 경로에서는 완성하지 못했으므로 현재 공항을 빼고 false 반환
    answer.pop_back();
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    vector<bool>visited(tickets.size()+1, false);
    
    // 0은 현재 사용한 티켓 수
    dfs(tickets, "ICN", visited, 0);
    
    return answer;
}
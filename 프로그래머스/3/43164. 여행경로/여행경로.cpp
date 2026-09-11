#include <string>
#include <vector>
#include <algorithm>

using namespace std;
vector<string> answer;

bool dfs(vector<vector<string>>& tickets, vector<bool> visited, string start, int cnt){
    if(cnt == tickets.size()) return true;
    
    for(int i = 0; i < tickets.size(); i++){
        if(!visited[i] && tickets[i][0] == start){
            visited[i] = true;
            answer.push_back(tickets[i][1]);
            if (dfs(tickets, visited, tickets[i][1], cnt+1)) return true;
            visited[i] = false;
            answer.pop_back();
        }
    }
    
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    vector<bool> visited(tickets.size()+1, false);
    answer.push_back("ICN");
    dfs(tickets, visited, "ICN", 0);    
    
    return answer;
}
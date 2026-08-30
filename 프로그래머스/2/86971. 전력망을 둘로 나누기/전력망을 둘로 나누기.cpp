#include <string>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

int bfs(int n, int cut_idx, vector<vector<int>> wires){
    vector<vector<int>> graph(n+1);
    for(int i = 0; i < wires.size(); i++){
        if(i==cut_idx) continue;
        
        int u = wires[i][0];
        int v = wires[i][1];
        
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    queue<int> q;
    vector<bool> visited(n+1, false);
    
    visited[1] = true;
    q.push(1);
    int cnt = 1;
    
    while(!q.empty()){
        int cur = q.front(); q.pop();
        
        for(int next: graph[cur]){
            if(!visited[next]){
                visited[next] = true;
                q.push(next);
                cnt++;
            }
        }
    }
    return cnt;
}




int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    for(int i = 0; i < wires.size(); i++){
        int cntA = bfs(n, i, wires);
        int cntB = n - cntA;
        
        answer = min(answer, abs(cntA-cntB));
    }
    
    return answer;
}
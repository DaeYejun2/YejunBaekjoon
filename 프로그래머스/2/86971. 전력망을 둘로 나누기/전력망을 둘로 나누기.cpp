#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;
int bfs(int n, int cuts_idx, vector<vector<int>> wires){
    vector<vector<int>> graph(n+1);
    for(int i = 0; i < wires.size(); i++){
        if(cuts_idx == i) continue;
        
        int u = wires[i][0];
        int v = wires[i][1];
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    queue<int> q;
    vector<bool> visited(n+1,false);
    int cnt = 1;
    q.push(1);
    visited[1]=true;
    
    while(!q.empty()){
        int cur = q.front(); q.pop();
        for(int next: graph[cur]){
            if(!visited[next]){
                cnt++;
                visited[next] = true;
                q.push(next);
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
        
        int diff = abs(cntA-cntB);
        answer = min(diff, answer);
    }
    
    return answer;
}
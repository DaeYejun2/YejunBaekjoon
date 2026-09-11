#include <string>
#include <vector>
#include <queue>

using namespace std;
int answer = 0; 

void bfs(vector<int>& visited, vector<vector<int>>& computers, int start, int n){
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while(!q.empty()){
        int cur = q.front(); q.pop();
        for(int next = 0; next < n; next++){
            if(!visited[next] && computers[cur][next] == 1){
                visited[next] = true;
                q.push(next);
            }
        }
    }
    answer++;
}

int solution(int n, vector<vector<int>> computers) {
    vector<int> visited(n, false);
    for(int i = 0; i < n; i++){
        if(!visited[i]){
            bfs(visited, computers, i, n);
        }
    }
    
    return answer;
}
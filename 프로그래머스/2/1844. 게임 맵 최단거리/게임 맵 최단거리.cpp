#include<vector>
#include<queue>
using namespace std;
int dy[4] = {1,-1,0,0};
int dx[4] = {0,0,1,-1};

int bfs(int startY, int startX, vector<vector<int>>& maps){
    int n = maps.size();  // 세로
    int m = maps[0].size();  // 가로
    
    vector<vector<int>> dist(n, vector<int>(m,-1));  // 방문, 누적값 지도
    queue<pair<int,int>> q;                          // 큐ㅋㅋ
    
    dist[startY][startX] = 1;
    q.push({startY, startX});
    
    while(!q.empty()){
        auto[y,x] = q.front(); q.pop();
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (ny < 0 || ny >= n || nx <0 || nx >= m) continue;
            if (maps[ny][nx] == 0) continue;
            if (dist[ny][nx] != -1) continue;

            dist[ny][nx] = dist[y][x] + 1;
            q.push({ny,nx});
        }
    }
    return dist[n-1][m-1] != -1 ? dist[n-1][m-1] : -1;
}



int solution(vector<vector<int>> maps)
{
    int answer = bfs(0,0,maps);
    return answer;
}
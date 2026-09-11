#include<vector>
#include<queue>
using namespace std;

int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

int bfs(int starty, int startx, vector<vector<int>>& maps){
    int n = maps.size(); int m = maps[0].size();
    queue<pair<int,int>> q;
    vector<vector<int>> dist(n, vector<int>(m,-1));
    
    q.push({starty,startx});
    dist[starty][startx] = 1;
    
    while(!q.empty()){
        auto[y,x] = q.front(); q.pop();
        for(int i = 0; i < 4; i++){
            int ny = dy[i] + y;
            int nx = dx[i] + x;
            
            if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
            if(maps[ny][nx] == 0) continue;
            if(dist[ny][nx] != -1) continue;
            
            dist[ny][nx] = dist[y][x] + 1;
            q.push({ny,nx});
        }
        
    }
    
    return dist[n-1][m-1];
}

int solution(vector<vector<int>> maps)
{
    return bfs(0,0,maps);
}
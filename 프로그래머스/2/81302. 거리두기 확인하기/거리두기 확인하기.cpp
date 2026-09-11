#include <string>
#include <vector>
#include <queue>

using namespace std;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,1,-1};

bool bfs(int startY, int startX, vector<string>& place){
    vector<vector<bool>> visited(5,vector<bool>(5,false));
    queue<tuple<int,int,int>> q;
    q.push({startY, startX, 0});
    visited[startY][startX] = true;
    
    while(!q.empty()){
        auto[y,x,dist] = q.front(); q.pop();
        if(dist >= 2) continue;
        
        for(int i = 0; i < 4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(ny < 0 || ny >= 5 || nx < 0 || nx >=5) continue;
            if(visited[ny][nx] || place[ny][nx] == 'X') continue;
            if(place[ny][nx] == 'P') return false;
            
            visited[ny][nx] = true;
            q.push({ny,nx,dist+1});
        }
        
    }
    
    return true;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    // 응시자 자리P, 빈 테이블 0, 파티션 X
    for(int i = 0; i < 5; i++){
        bool isValid = true;
        for(int j = 0; j < 5; j++){
            for(int k = 0; k < 5; k++){
                if(places[i][j][k] == 'P')
                    if(!bfs(j,k,places[i])){
                        isValid = false;
                        break;
                    }
            }
            if(!isValid) break;
        }
        answer.push_back(isValid ? 1: 0);
    }
    
    
    return answer;
}
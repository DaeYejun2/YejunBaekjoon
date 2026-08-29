#include <string>
#include <vector>
#include <queue>

using namespace std;
const int MAX_SIZE = 102;
int board[MAX_SIZE][MAX_SIZE] = {0};
int visited[MAX_SIZE][MAX_SIZE] = {0};

int dy[4] = {-1,1,0,0};
int dx[4] = {0,0,-1,1};

void drawRectangle(vector<vector<int>>& rectangle){
    for(const auto& rec: rectangle){
        // 좌표 2배 확대
        int x1 = rec[0]*2;
        int y1 = rec[1]*2;
        int x2 = rec[2]*2;
        int y2 = rec[3]*2;
        
        for(int y = y1; y <= y2; y++){
            for(int x = x1; x <= x2; x++){
                if (board[y][x] == 2) continue;
                if(x == x1 || x == x2 || y == y1 || y == y2) board[y][x] = 1;
                else board[y][x] = 2;
            }
        }
    }
}

int bfs(int startX, int startY, int itemX, int itemY){
    queue<pair<int,int>> q;
    // 시작/도착 좌표도 2배
    startX*=2; startY*=2;
    itemX*=2; itemY*=2;
    
    q.push({startY, startX});
    visited[startY][startX] = 1; // 시작점 방문 표시 -> 얘로 거리 나타내는 듯
    
    while(!q.empty()){
        auto[cy, cx] = q.front(); q.pop();
        
        if(cx == itemX && cy == itemY)
            // 구한 거리에서 시작점(1)을 빼고, 2배 확대한 스케일을 다시 원래대로 돌리기 위함.
            return(visited[cy][cx] - 1) / 2;
        
        for(int i = 0; i < 4; i++){
            int ny = cy+dy[i]; int nx = cx+dx[i];
            
            if(ny < 0 || ny >= MAX_SIZE || nx < 0 || nx >= MAX_SIZE) continue;
            if(board[ny][nx] == 1 && visited[ny][nx] == 0){
                visited[ny][nx] = visited[cy][cx] + 1;
                q.push({ny,nx});
            }
        }
    }
    return -1;    
}



int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    drawRectangle(rectangle);
    int answer = bfs(characterX, characterY, itemX, itemY);
    return answer;
}
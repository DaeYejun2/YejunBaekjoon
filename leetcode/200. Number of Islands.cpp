int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size(); int m = grid[0].size();
        queue<pair<int,int>> q;
        int cnt = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == '1'){
                    q.push({i,j});
                    grid[i][j] = '0';
                    while(!q.empty()){
                        auto[y,x] = q.front(); q.pop();
                        for(int k = 0; k < 4; k++){
                            int ny = y + dy[k];
                            int nx = x + dx[k];

                            if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                            if (grid[ny][nx] == '0') continue;

                            q.push({ny, nx});
                            grid[ny][nx] = '0';
                        }
                    }
                    cnt++;
                }
            }
        }
        return cnt;
    }
};

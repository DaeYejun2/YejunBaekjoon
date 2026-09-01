#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0; int n = board.size();
    vector<int> v;
    for(int m: moves){
        m -= 1;
        for(int y = 0; y < n; y++){
            if(board[y][m] > 0) {
                int tmp = board[y][m];
                board[y][m] = 0;
                if(!v.empty() && v.back() == tmp) {
                    v.pop_back();
                    answer+=2;
                }
                else {
                    v.push_back(tmp);
                }
                break;
            }
        }
    }
    
    return answer;
}
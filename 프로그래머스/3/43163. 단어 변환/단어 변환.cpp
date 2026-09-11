#include <string>
#include <vector>
#include <queue>

using namespace std;
int answer = 101;

void bfs(string start, string target, vector<string>& words){
    queue<pair<string, int>> q;
    q.push({start, 0});
    vector<bool>visited(words.size(), false);
    
    while(!q.empty()){
        auto& [cur, idx] = q.front(); q.pop();
        if (cur==target){
            answer = min(answer, idx);
            continue;
        }
        for(int j = 0; j < words.size(); j++){
            int diff = 0;
            for(int i = 0; i < cur.length(); i++){
                if (cur[i] != words[j][i]) diff++;
            }
            if(!visited[j] && diff == 1){
                visited[j] = true;
                q.push({words[j], idx+1});
            }
        }
    }
    if (answer == 101) answer = 0;
}

int solution(string begin, string target, vector<string> words) {
    bfs(begin, target, words);
    
    return answer;
}
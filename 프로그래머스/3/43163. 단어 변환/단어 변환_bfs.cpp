#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

bool is_one_diff(string& a, string& b){
    int diff = 0;
    for(int i = 0; i < a.length(); i++){
        if (a[i] != b[i]) diff++;
        if(diff > 1) return false;
    }
    return diff == 1;
}


int solution(string begin, string target, vector<string> words) {
    if (find(words.begin(), words.end(), target) == words.end()) return 0;
    // queue는 {현재 단어, 변환 횟수로}
    queue<pair<string, int>> q;
    vector<bool>visited(words.size(), false);
    
    q.push({begin, 0});
    while(!q.empty()){
        string cur = q.front().first;
        int count = q.front().second;
        // auto[cur, count] = q.front();
        q.pop();
        
        if(cur == target) return count;
        
        for(int i = 0; i < words.size(); i++){
            if(!visited[i] && is_one_diff(cur, words[i])){
                visited[i] = true;
                q.push({words[i], count+1});
            }
        }
    }
    
    return 0;
}

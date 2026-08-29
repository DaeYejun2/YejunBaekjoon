#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int min_answer = 51;

bool is_one_diff(string& a, string& b){
    int diff = 0;
    for(int i = 0; i < a.length(); i++){
        if (a[i] != b[i]) diff++;
        if(diff > 1) return false;
    }
    return diff == 1;
}

void dfs(string cur, string target, vector<string> words, vector<bool>visited, int count){
    if(cur == target){
        min_answer = min(min_answer, count);
        return;
    }
    if(count >= min_answer) return;
    
    for(int i = 0; i < words.size(); i++){
        if(!visited[i] && is_one_diff(words[i], cur)){
            visited[i] = true;
            dfs(words[i], target, words, visited, count+1);
            visited[i] = false;
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    vector<bool>visited(words.size(), false);
    if(find(words.begin(), words.end(), target) == words.end()) return 0;
    dfs(begin, target, words, visited, 0);
    return min_answer;
}
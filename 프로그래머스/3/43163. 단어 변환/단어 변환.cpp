#include <string>
#include <vector>
#include <algorithm>

using namespace std;
// 단어 최대 개수가 50개. 나올 수 없는 큰 값으로 초기화
int min_answer = 51;

// 1글자만 다른지 확인하는 함수
bool is_one_diff(const string& a, const string& b){
    int diff = 0;
    for(int i = 0; i < a.length(); i++){
        if(a[i] != b[i]) diff++;
        if(diff > 1) return false;
    }
    return diff == 1;
}

void dfs(string cur, string target, vector<string>& words, vector<bool>& visited, int count){
    if (cur == target){
        min_answer = min(min_answer, count);
        return;
    }
    if(count >= min_answer) return;
    
    for(int i = 0; i < words.size(); i++){
        if(!visited[i] && is_one_diff(cur, words[i])){
            visited[i] = true;
            dfs(words[i], target, words, visited, count+1);
            visited[i] = false;
        }
    }
    
}

int solution(string begin, string target, vector<string> words) {
    if(find(words.begin(), words.end(), target)==words.end()) return 0;
    
    vector<bool> visited(words.size(), false);
    
    dfs(begin, target, words, visited, 0);
    return min_answer;
}
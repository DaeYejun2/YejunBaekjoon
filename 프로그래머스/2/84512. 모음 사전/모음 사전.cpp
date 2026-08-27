#include <string>
#include <vector>

using namespace std;
int cnt = 0;
int answer = 0;
char vowels[5] = {'A', 'E', 'I', 'O', 'U'};

void dfs(string cur, string target){
    if(cur != ""){
        cnt++;
        if (cur == target){
            answer = cnt;
            return;
        }
    }
    if(cur.length() == 5) return;
    for(int i = 0; i < 5; i++){
        dfs(cur+vowels[i], target);
    }
    
}

int solution(string word) {
    dfs("", word);
    return answer;
}
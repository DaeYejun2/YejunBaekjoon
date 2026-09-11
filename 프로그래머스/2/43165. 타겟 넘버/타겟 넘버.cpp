#include <string>
#include <vector>

using namespace std;
int cnt = 0;

void dfs(int target, vector<int>& numbers, int n, int idx, int cur){
    if(idx == n){
        if(target == cur){
            cnt++;
            return;
        }
    return;
    }
    
    // if(cur >= target) return;
    dfs(target, numbers, n, idx+1, cur+numbers[idx]);
    dfs(target, numbers, n, idx+1, cur-numbers[idx]);
    
}

int solution(vector<int> numbers, int target) {
    int n = numbers.size();
    dfs(target, numbers, n, 0, 0);
    return cnt;
}
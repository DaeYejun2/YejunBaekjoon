#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool is_prime(int n){
    if(n < 2) return false;
    for(int i = 2; i < n; i++){
        if (n % i == 0) return false;
    }
    return true;  // 소수노!
}

void dfs(string& numbers, string cur, unordered_set<int>& unique_nums, vector<bool>& visited){
    // 빈문자열이 아니면 unique에 넣기
    if(!cur.empty()) unique_nums.insert(stoi(cur));
    
    for(int i = 0; i < numbers.length(); i++){
        if(!visited[i]){
            visited[i] = true;
            dfs(numbers, cur+numbers[i], unique_nums, visited);
            visited[i] = false;
        }
    }
}

int solution(string numbers) {
    int answer = 0;
    unordered_set<int> unique_nums;
    vector<bool> visited(numbers.length(), false);
    
    // 백트래킹으로 만들 수 있는 모든 수 생성
    dfs(numbers, "", unique_nums, visited);
        
    for(int n: unique_nums)
        if(is_prime(n)) answer++;
    
    
    return answer;
}
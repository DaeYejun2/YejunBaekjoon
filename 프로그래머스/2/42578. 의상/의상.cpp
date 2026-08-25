#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> counts;
    for(auto c: clothes){
        counts[c[1]]++;      // 의상의 종류.  counts는 의상의 종류, 갯수
    }
    
    for(auto[type, cnt]: counts){
        answer *= (cnt+1);
    }
    
    
    return answer-1;
}
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(), citations.end(), [](int& a, int& b){
        return a > b;
    });
    // 6 5 3 1 0
    for(int i = 0; i < citations.size(); i++){  
        // i번째 논문의 인용 횟수가 (i+1)이상이면, 
        // 최소 (i+1)편의 논문이 (i+1)회 이상 인용된 것임
        if (citations[i] >= i+1){
            answer = i+1;
        }
        else break;
    }
    
    
    return answer;
}
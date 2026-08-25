#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    int ln = prices.size();
    vector<int> answer(ln);
    stack<int> s;       // 인덱스를 저장
    
    for(int i = 0; i < ln; i++){
        // 현재 가격이 이전 가격보다 떨어졌다면 스택에서 꺼내며 정산
        while(!s.empty() && prices[s.top()] > prices[i]){
            int prev_idx = s.top();
            s.pop();
            answer[prev_idx] = i - prev_idx;    // 버틴 시간 = 현재 시점 - 과거 시점
        }
        s.push(i);      // 정산했으니 현재 시점 다시 추가
    }
    // 끝까지 가격이 떨어지지 않고 남아있는 시점들 정산
    while (!s.empty()){
        int prev_idx = s.top();
        s.pop();
        answer[prev_idx] = (ln-1) - prev_idx;
        // 배열의 맨 마지막 순간까지도 가격이 떨어지지 않은 것이니 마지막 인덱스 - 과거 시점 개념으로 보면 될 듯
    }
    
    return answer;
}

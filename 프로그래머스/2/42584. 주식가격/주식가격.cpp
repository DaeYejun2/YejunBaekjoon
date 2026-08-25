#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    int ln = prices.size();
    vector<int> answer(ln);
    
    for (int i = 0; i < ln; i++){
        for (int j = i+1; j < ln; j++){
            answer[i]++;
            if (prices[i] > prices[j]) break;
        }
    }
    
    return answer;
}
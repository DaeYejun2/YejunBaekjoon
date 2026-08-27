#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> v1 = {1,2,3,4,5}; int a1=0;
    vector<int> v2 = {2,1,2,3,2,4,2,5}; int a2=0;
    vector<int> v3 = {3,3,1,1,2,2,4,4,5,5}; int a3=0;
    
    for(int i = 0; i < answers.size(); i++){
        if (answers[i] == v1[i%v1.size()]) a1++;
        if (answers[i] == v2[i%v2.size()]) a2++;
        if (answers[i] == v3[i%v3.size()]) a3++;
    }
    int max_score = max({a1,a2,a3});
    if(a1==max_score) answer.push_back(1);
    if(a2==max_score) answer.push_back(2);
    if(a3==max_score) answer.push_back(3);
    
    return answer;
}
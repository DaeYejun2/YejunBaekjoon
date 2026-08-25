#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer;
    unordered_map<string, int> m;
    
    for(string s: participant){
        m[s]++;
    }
    for (string c: completion){
        m[c]--;
    }
    
    for(auto [k, v] : m){
        if (v > 0){
            answer = k;
            break;
        }
    }
    
    return answer;
}
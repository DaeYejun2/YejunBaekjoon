#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone) {
    unordered_set<string> s(phone.begin(), phone.end());
    for (string p: phone){
        string prefix = "";
        for (int i = 0; i < p.size() - 1; i++){
            prefix += p[i];
            if(s.count(prefix)) return false;
        }
    }
    
    return true;
}
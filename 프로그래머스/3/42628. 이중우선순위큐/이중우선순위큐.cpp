#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<string> operations) {
    multiset<int> ms;
    for(const string& op: operations){
        char cmd = op[0];
        int num = stoi(op.substr(2));
        
        if(cmd == 'I') ms.insert(num);
        else{
            if(!ms.empty()){
                if (num == 1) ms.erase(prev(ms.end()));
                else ms.erase(ms.begin());
            }
        }
    }
    
    if(ms.empty()) return {0,0};
    return{*prev(ms.end()), *ms.begin()};
}
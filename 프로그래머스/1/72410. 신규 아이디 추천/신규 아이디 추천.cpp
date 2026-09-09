#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {

    for(int i =  0; i < new_id.length(); i++){
        if (new_id[i] >='A' && new_id[i] <= 'Z')
            new_id[i] += 32;
    }
    
    string step2 = "";
    for(char c: new_id){
        if(isdigit(c) || islower(c) || c == '-' || c == '_' || c == '.')
            step2+=c;
    }
    
    string step3 = "";
    for(char c: step2)
        if(c == '.'){
            if(step3.empty() || step3.back() != '.') step3 += c;
        }
        else step3 += c;
    
    if(!step3.empty() && step3.front() == '.') step3.erase(step3.begin());
    if(!step3.empty() && step3.back() == '.') step3.pop_back();
    
    if(step3.empty()) step3 += 'a';
    
    if(step3.length() >= 16){
        step3 = step3.substr(0,15);
        if(step3.back() == '.') step3.pop_back();
    }
    
    while(step3.length() < 3) step3+=step3.back();
    
    
    return step3;
}
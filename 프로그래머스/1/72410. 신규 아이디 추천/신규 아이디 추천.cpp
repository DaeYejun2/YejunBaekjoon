#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string new_id) {
    
    // 1. 대문자 -> 소문자 치환
    for(char &c: new_id){
        c = tolower(static_cast<unsigned char>(c));
    }
    // 이렇게도 된다. 숙지해둘 것.
    // for(int i = 0; i < new_id.size(); ++i)
    //     if(new_id[i] >= 'A' && new_id[i] <= 'Z')
    //         new_id[i] += 32;

    // 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    string step2="";
    for(char c: new_id){
        if(islower(static_cast<unsigned char>(c)) ||
            isdigit(static_cast<unsigned char>(c)) ||
           c == '-' || c == '_' || c=='.') {
               step2 += c;
           }
    }
    
    // 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    string step3="";
    for(char c: step2){
        if(c == '.'){
            if (step3.empty() || step3.back() != '.') step3 += c;
        }
        else step3 += c;
    }
    
    // 4. 마침표가 처음이나 끝에 위치한다면 제거   erase 중요
    if(!step3.empty() && step3.front() == '.') step3.erase(step3.begin());
    if(!step3.empty() && step3.back() == '.') step3.pop_back();
    
    // 5. 빈 문자열이라면 'a' 대입
    if(step3.empty()) step3 = "a";
    
    // 6. 길이가 16자 이상이면 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    // 만약 제거 후 마침표(.)가 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거    
    if(step3.length() >= 16) {
        step3 = step3.substr(0,15);
        if(step3.back() == '.') step3.pop_back();
    }
    
    // 7. 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while(step3.length() < 3) step3 += step3.back();
    
    return step3;
}
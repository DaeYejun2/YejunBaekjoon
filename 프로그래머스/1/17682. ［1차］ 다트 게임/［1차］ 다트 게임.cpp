#include <string>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    int val = 0;
    int prev = 0;
    bool star_chk = false;
    bool sharp_chk = false;
    for(int i = 0; i < dartResult.length(); i++){
        if (star_chk){
            answer -= prev;
            prev *= 2;
            answer += prev;
            answer -= val;
            val *= 2;
            answer += val;
            star_chk = false;
        }
        else if (sharp_chk){
            answer -= val * 2;
            val *= -1;
            sharp_chk = false;
        }
        if (isdigit(dartResult[i])) {
                if(i < dartResult.length() -1 && dartResult[i] == '1' && dartResult[i+1] == '0'){
                    i++;
                    val = 10;
                }
                else {
                    prev = val;
                    val =dartResult[i] - '0';
            }
        }
        
        
        if(dartResult[i] == 'S'){
            answer += val;
        }
        else if (dartResult[i] == 'D'){
            val = val * val;
            answer += val;
        }
        else if (dartResult[i] == 'T'){
            val = val * val * val;
            answer += val;
        }

        else if (dartResult[i] == '*'){
            star_chk = true;
        }
        else if (dartResult[i] == '#'){
            sharp_chk = true;
        }
    }
    
    if (star_chk){
            answer += prev;
            answer += val;
        }
    if (sharp_chk){
            answer -= val * 2;
            val *= -1;
        }
    
    return answer;
}
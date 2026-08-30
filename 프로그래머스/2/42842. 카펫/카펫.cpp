#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(int brown, int yellow) {
    int total = brown+yellow;
    
    for(int h = 3; h <= sqrt(total); h++){   // h는 3부터
        if(total % h == 0){
            int w = total / h;
            if((w-2)*(h-2) == yellow) return{w,h};
        }
    }
    return {0,0};
}
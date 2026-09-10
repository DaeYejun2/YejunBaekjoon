#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    int tot = brown+yellow;
        
    for(int x = 1; x <= tot; x++){
        int y = tot/x;
        if(x*y == tot && (x-2) * (y-2) == yellow) return {y,x};
    }

}
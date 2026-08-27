#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    int total = brown + yellow;
    // 따라서 노란색 격자의 가로는 W - 2, 세로는 H - 2가 되며,
    // (W - 2) * (H - 2) = yellow를 만족해야 합니다.
    // H의 최솟값은 3부터 시작.
    for(int i = 3; i < total; i++){
        if(total % i == 0) {
            int tmp = total / i;
            if((tmp-2)*(i-2) == yellow) return {tmp,i};
        }
    }

}
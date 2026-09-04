#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(string dartResult) {
    vector<int> scores;

    for (int i = 0; i < dartResult.length(); i++) {
        // 1. 점수 파싱 (10점 예외 처리 포함)
        if (isdigit(dartResult[i])) {
            int score = 0;
            if (dartResult[i] == '1' && dartResult[i + 1] == '0') {
                score = 10;
                i++; // '0'까지 건너뜀
            } else {
                score = dartResult[i] - '0';
            }
            scores.push_back(score);
        }
        // 2. 보너스 (S, D, T)
        else if (dartResult[i] == 'S') {
            // 그대로 유지 (1제곱)
        } else if (dartResult[i] == 'D') {
            scores.back() = scores.back() * scores.back();
        } else if (dartResult[i] == 'T') {
            scores.back() = scores.back() * scores.back() * scores.back();
        }
        // 3. 옵션 (*, #) - 과거를 롤백할 필요 없이 배열 원소만 조작
        else if (dartResult[i] == '*') {
            scores.back() *= 2;
            if (scores.size() >= 2) {
                scores[scores.size() - 2] *= 2;
            }
        } else if (dartResult[i] == '#') {
            scores.back() *= -1;
        }
    }

    // 4. 3번의 점수 합산
    int answer = 0;
    for (int s : scores) answer += s;
    return answer;
}

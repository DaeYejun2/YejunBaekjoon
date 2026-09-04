#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

// 파일 정보를 담을 구조체
struct File {
    string original; // 정답 반환용 원본 문자열
    string head;     // 소문자로 변환된 HEAD
    int number;      // 정수로 변환된 NUMBER
};

// 정렬 기준을 정의하는 비교 함수
bool cmp(const File& a, const File& b) {
    if (a.head != b.head) {
        return a.head < b.head; // 1순위: HEAD 사전순 비교
    }
    if (a.number != b.number) {
        return a.number < b.number; // 2순위: NUMBER 숫자 크기 비교
    }
    return false; // 3순위: 둘 다 같으면 stable_sort가 기존 순서 유지
}

vector<string> solution(vector<string> files) {
    vector<File> parsed_files;

    for (string file : files) {
        int n = file.length();
        int idx = 0;

        // 1. HEAD 파싱: 숫자가 나오기 전까지
        string head = "";
        while (idx < n && !isdigit(file[idx])) {
            head += tolower(file[idx]); // 대소문자 무시를 위해 소문자로 변환
            idx++;
        }

        // 2. NUMBER 파싱: 숫자가 시작되고 최대 5자리까지
        string num_str = "";
        while (idx < n && isdigit(file[idx]) && num_str.length() < 5) {
            num_str += file[idx];
            idx++;
        }

        // 구조체에 담아서 벡터에 추가 (TAIL은 정렬에 쓰이지 않으므로 무시)
        parsed_files.push_back({file, head, stoi(num_str)});
    }

    // 3. stable_sort를 이용해 정렬
    stable_sort(parsed_files.begin(), parsed_files.end(), cmp);

    // 4. 정렬된 결과에서 원본 파일명만 다시 추출
    vector<string> answer;
    for (const auto& f : parsed_files) {
        answer.push_back(f.original);
    }

    return answer;
}
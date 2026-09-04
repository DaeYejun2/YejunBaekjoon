#include <string>
#include <vector>
#include <cmath>

using namespace std;

pair<int, int> pos[12] = {
    {3,1}, // 0
    {0,0}, {0,1}, {0,2}, // 1,2,3
    {1,0}, {1,1}, {1,2}, // 4,5,6
    {2,0}, {2,1}, {2,2}, // 7,8,9
    {3,0}, // *: 왼손 시작점 10
    {3,2}, // #: 오른손 시작점 11
};

// 맨해튼 거리로 좌표 거리 계산
int get_dist(pair<int,int> a, pair<int,int> b){
    return abs(a.first - b.first) + abs(a.second - b.second);
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    
    pair<int,int> left_pos = pos[10];  // * 위치
    pair<int,int> right_pos = pos[11]; // # 위치
    
    for(int num: numbers){
        if(num == 1 || num == 4 || num == 7){
            answer += 'L';
            left_pos = pos[num];
        }
        else if(num == 3 || num == 6 || num == 9){
            answer += 'R';
            right_pos = pos[num];
        }
        else{
            int left_dist = get_dist(left_pos, pos[num]);
            int right_dist = get_dist(right_pos, pos[num]);
            
            if (left_dist < right_dist){
                answer += 'L';
                left_pos = pos[num];
            }
            else if(right_dist < left_dist){
                answer += 'R';
                right_pos = pos[num];
            }
            else{
                if (hand == "left"){
                    answer += 'L';
                    left_pos = pos[num];
                }
                else{
                    answer += 'R';
                    right_pos = pos[num];
                }
            }
        }
    }
    return answer;
}
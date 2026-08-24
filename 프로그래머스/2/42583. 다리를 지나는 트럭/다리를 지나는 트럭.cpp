#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    queue<int> bridge;
    // 다리 길이만큼 0으로 채워 초기화
    for(int i = 0; i < bridge_length; i++) bridge.push(0);
    
    int cnt = 0;    // 경과 시간
    int w = 0;      // 다리 위 총 무게
    int idx = 0;    // 대기 중인 트럭 인덱스
    
    // 대기 중인 모든 트럭이 다리에 올라갈 때까지 반복
    while(idx < truck_weights.size()){
        cnt++;
        
        // 1. 다리 맨 앞 칸에서 트럭(또는 빈 공간 0) 빠져나감
        w -= bridge.front();
        bridge.pop();
        
        // 2. 다음 트럭이 다리에 올라올 수 있는지 확인
        if (w + truck_weights[idx] <= weight){
            bridge.push(truck_weights[idx]);
            w += truck_weights[idx];
            idx++;
        }
        else{
            // 무게 초과로 못 온다면
            bridge.push(0);
        }
    }
    
    return cnt + bridge_length;
}
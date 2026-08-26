#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    // 요청시간 짧은 순으로만 하면 아직 요청 시간조차 되지 않은 작업이 소요시간이 짧다는 이유로
    // 먼저 실행할 수도 있음.  요청 시점 기준 오름차순 정렬
    sort(jobs.begin(), jobs.end());
    
    // {소요 시간, 요청 시점} 최소힙  - 대기열이라고 보면될 듯
    priority_queue<pair<int,int>,vector<pair<int,int>>, greater<pair<int,int>>> pq;
    
    int time = 0;  //현재 시각
    int idx = 0;   // jobs 배열 인덱스
    int count = 0;   // 완료된 작업 수

    while(count < jobs.size()){   // 이거는 작업 수 만큼 반복. pq.empty 쓰면 대기 시간동안 오류 날 수도
        // 현재 시점(time) 이하로 요청된 모든 작업을 큐에 삽입
        while (idx < jobs.size() && jobs[idx][0] <= time){
            pq.push({jobs[idx][1], jobs[idx][0]});  // {소요시간, 요청시점}
            idx++;
        }
        
        if (!pq.empty()){  // 대기열에 작업이 있을 때
            //작업 수행: 소요 시간이 가장 짧은 것부터 꺼냄
            int duration = pq.top().first;
            int request_time = pq.top().second;
            pq.pop();
            
            time += duration;
            answer += (time - request_time);  // 0번 작업 3ms - 2번 작업 요청 시간 3ms = 0 
            // => 겹치는 시간 없이 바로 시작
            count++;
        }
        // 처리할 수 있는 작업이 없다면 다음 작업의 요청 시점으로 시간 점프. 
        else time = jobs[idx][0];
    }
    
    return answer / jobs.size();
}
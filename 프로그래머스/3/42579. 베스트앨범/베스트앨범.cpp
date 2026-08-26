#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, int> genres_play;     // 장르별 총 재생수를 구하기 위한 map
    unordered_map<string, vector<pair<int,int>>> song_list; // (장르, {재생수, 고유번호})
    
    for (int i = 0; i < genres.size(); i++){
        genres_play[genres[i]] += plays[i];
        song_list[genres[i]].push_back({plays[i], i});
    }
    
    // 장르별 총 재생수 기준 정렬을 위해 vector로 복사 -> map은 정렬이 안되기 때문 
    vector<pair<string, int>> sorted_genres(genres_play.begin(), genres_play.end());
    sort(sorted_genres.begin(), sorted_genres.end(), [](auto& a, auto& b){
        return a.second > b.second;     // 재생수 내림차순
    });
    
    // 정렬된 장르 순서대로 수록곡 선택
    for (auto& [genre, total_play]: sorted_genres) {
        auto& songs = song_list[genre];  // 장르의 재생수와 고유번호가 들어가죠
        
        // 장르 내 곡 정렬
        sort(songs.begin(), songs.end(), [](auto& a, auto&& b){
            return a.first == b.first ? a.second < b.second : a.first > b.first;
        });  // 재생 수가 같으면 고유번호 오름차순 , 다르면 재생 수 내림차순
        
        for(int i = 0; i < songs.size() && i < 2; i++)
            answer.push_back(songs[i].second);
    }
    
    
    return answer;
}
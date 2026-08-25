#include <vector>
#include <unordered_set>
using namespace std;

int solution(vector<int> nums)
{
    unordered_set<int> s(nums.begin(), nums.end());
    int answer = 0;
    if (s.size() >= nums.size()/2) answer = nums.size()/2;
    else answer = s.size();
    
    return answer;
}
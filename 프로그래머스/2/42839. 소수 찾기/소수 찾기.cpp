#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

int solution(string numbers) {
    int answer = 0;
    int n = 9999999;
    vector<bool> is_prime(n+1, true);
    is_prime[0] = false; is_prime[1] = false;
    
    for(int i = 2; i*i<=n; i++){
        if(is_prime[i]){
            for(int j = i*i; j <= n; j+=i){
                is_prime[j] = false;
            }
        }
    }
    unordered_set<int> unique_nums;
    sort(numbers.begin(), numbers.end());
    
    do{
        for(int len = 1; len <= numbers.size(); len++){
            int num = stoi(numbers.substr(0,len));
            unique_nums.insert(num);
        }
    }while(next_permutation(numbers.begin(), numbers.end()));

    for(int n: unique_nums){
        if(is_prime[n]) answer++;
    }
    
    return answer;
}
class MedianFinder {
public:
    // 작은 쪽 절반을 저장하는 최대 힙
    priority_queue<int> max_heap;
    // 큰 쪽 절반을 저장하는 최소 힙
    priority_queue<int, vector<int>, greater<int>> min_heap;
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        // 일단 max_heap에 넣고 최댓값을 min_heap으로 넘김
        max_heap.push(num);
        min_heap.push(max_heap.top());
        max_heap.pop();

        // 2. max_heap 크기가 min_heap보다 크거나 같도록 균형 유지
        if(min_heap.size() > max_heap.size()){
            max_heap.push(min_heap.top());
            min_heap.pop();
        }
    }
    
    double findMedian() {
        if(max_heap.size() > min_heap.size())
            return max_heap.top();
        return (max_heap.top() + min_heap.top()) / 2.0;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

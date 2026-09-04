class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        stack<int> st;
        int max_rec = 0;

        for(int i = 0; i < heights.size(); i++){
            while(!st.empty() && heights[st.top()] >= heights[i]){ 
                int h = heights[st.top()];       
                st.pop();

                int width = st.empty() ? i : (i - st.top() - 1);
                max_rec = max(max_rec, h * width);
            }
            st.push(i);
        }
        return max_rec;
    }
};

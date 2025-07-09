class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> positive;
        vector<int> negative;
        vector<int> result;
        for (int n : nums){
            if (n > 0){
                positive.push_back(n);
            }else{
                negative.push_back(n);
            }
        }
        int i = 0;
        int j = 0;
        while( i < positive.size() && j < negative.size()){
            result.push_back(positive[i]);
            result.push_back(negative[j]);
            i++;
            j++;
        }
        // If there are any leftover elements
        while (i < positive.size()){
            result.push_back(positive[i]);
            i++;
        }
        while (j < negative.size()){
            result.push_back(negative[i]);
            j++;
        }
        return result;
    }
};
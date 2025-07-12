class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> frequency;
        vector<int> result;

        for (int num : nums) {
            frequency[num]++;
        }

        for (auto& pair : frequency) {
            if (pair.second > n / 3) {
                result.push_back(pair.first);
            }
        }

        return result;

    }
};
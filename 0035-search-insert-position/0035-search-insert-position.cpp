class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int low  = 0;
        int high = n - 1;
        int insertion_index = n;
        while (low <= high){
            int mid = low + (high - low) / 2;
            if (nums[mid] >= target){
                insertion_index = mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
            
        }
        return insertion_index;
    }
};
class Solution {
    public int maxProduct(int[] nums) {
        int result = nums[0];

        int n = nums.length;
        for (int i = 0;i<n; i++){
            int p = nums[i];
            for(int j = i + 1; j < n; j++){
                result = Math.max(result, p);

                p *= nums[j];
            }
            result = Math.max(result, p);
        }
        return result;
    }
}
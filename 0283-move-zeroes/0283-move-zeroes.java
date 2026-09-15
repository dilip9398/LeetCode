class Solution {
    public void moveZeroes(int[] nums) {
        int c = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != 0) {
                int t = nums[j];
                nums[j] = nums[c];
                nums[c] = t;
                c++;

            }
        }
    }
}
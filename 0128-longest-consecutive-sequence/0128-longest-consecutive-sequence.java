class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        if (n < 0) return 0;
        Arrays.sort(nums);
        int longest = 0;
        int cnt = 0;
        int ls = Integer.MIN_VALUE;

        for(int i = 0;   i < n; i++){

            if (nums[i] - 1 == ls){
                cnt += 1;
                ls = nums[i];
            }else if (nums[i] != ls){
                cnt = 1;
                ls = nums[i];
            }
            longest = Math.max(longest, cnt);
        }
        return longest;
    }
}
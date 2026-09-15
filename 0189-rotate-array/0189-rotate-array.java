class Solution {

    public void reversearrar(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;

        }
    }

    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;

        reversearrar(nums, n-k, n-1);
        reversearrar(nums, 0, n - k - 1);
        reversearrar(nums, 0, n - 1);
    }
}
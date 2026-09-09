class Solution {
    public int[] getConcatenation(int[] arr) {
        int n = arr.length;

        int[] ans = new int[arr.length * 2];

        for (int i = 0; i < n; i++) {
            ans[i] = arr[i];
        }
        for (int i = 0; i < n; i++) {
            ans[n + i] = arr[i];
        }
        return ans;
    }
}

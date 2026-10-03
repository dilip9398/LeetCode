class Solution {

    // Time: O(log n)
    // Space: O(1)

    public int search(int[] nums, int target) {

        return  roated_Search(nums,0,nums.length-1,target);
    
    }
    public static int roated_Search(int arr[],int si,int ei,int tar){
        if (si > ei) {
            return -1;
        }
        int mid = si + (ei - si) / 2;
        if (arr[mid] == tar) {
            return mid;
        }

        // mid in Line 1
        if (arr[si] <= arr[mid]) {
            // case 1: left of the mid
            if (arr[si] <= tar && tar <= arr[mid]) {
                return roated_Search(arr, si, mid - 1, tar);
            } else {
                return roated_Search(arr, mid + 1, ei, tar);
            }
        } else {
            // mid in Line 2
            // case 1: right of the mid
            if (arr[ei] >= tar && tar >= arr[mid]) {
                return roated_Search(arr, mid + 1, ei, tar);
            } else {
                return roated_Search(arr, si, mid - 1, tar);
            }
        }
    }
}
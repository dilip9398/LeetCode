class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        int arr [] = new int [m+n];
        int k =0;
        int i = 0, j=0;
        while(i<m){
            arr[k++] = nums1[i++];
        }
        while(j<n){
            arr[k++] = nums2[j++];
        }
        Arrays.sort(arr);
        for(i = 0; i< m+n;i++){
            nums1[i] = arr[i];
        }
        
    }
}
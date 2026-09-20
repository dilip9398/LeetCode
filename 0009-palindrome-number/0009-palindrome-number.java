class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false;
        }
        int original = x;
        int sum = 0;
        int rem = 0;
        while (x > 0) {
            rem = x % 10;
            x = x / 10;
            sum = sum * 10 + rem;

        }
        return (original == sum);
    }
}
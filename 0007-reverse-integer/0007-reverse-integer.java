class Solution {
    public int reverse(int x) {
        int original = x;
        long sum = 0;
        if(x < 0){
            x = (-1)*x;
        }
        while(x>0){
            int d = x % 10;
            sum = sum * 10 + d;
            x /= 10;
        }
        if (sum > Integer.MAX_VALUE || sum < Integer.MIN_VALUE){
            return 0;
        }
        else if (original < 0){
            return (-1)*(int)sum;
        }
        else{
            return (int)sum;
        }
    }
}
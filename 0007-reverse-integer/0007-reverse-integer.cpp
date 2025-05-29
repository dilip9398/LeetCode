#include <climits> // For INT_MIN and INT_MAX

class Solution {
public:
    int reverse(int x) {
        long sum = 0;
        while (x != 0) {
            int digit = x % 10;
            sum = sum * 10 + digit;
            x /= 10;
        }
        if (sum < INT_MIN || sum > INT_MAX) {
            return 0;
        }
        return (int)sum;
    }
};

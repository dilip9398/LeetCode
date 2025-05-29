class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0
        while x > 0:
            rem = x % 10
            reverse = reverse * 10 + rem
            x = x // 10
        reverse *= sign
        if reverse < -2**31 or reverse > 2**31 - 1:  # Overflow check
            return 0
        return reverse
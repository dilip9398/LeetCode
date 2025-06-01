class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([ch.lower() for ch in s if ch.isalnum()])

        # def palindrome(s , i):
        #     if (i >= len(s)/2): return True
        #     if (s[i] != s[len(s)-i-1]):
        #         return False
        #     return palindrome(s, i+1)

        # return palindrome(s, 0)


        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
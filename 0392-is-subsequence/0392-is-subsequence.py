class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        n2 = len(t)
        i = 0
        j = 0
        while i < n and j < n2:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return n == i
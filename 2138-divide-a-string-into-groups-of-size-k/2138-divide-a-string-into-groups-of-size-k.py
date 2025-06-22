class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        n = len(s)
        ans = []

        while len(s) % k != 0:
            s += fill

        for i in range(0, n, k):
            ans.append(s[i:i + k])

        return ans
        
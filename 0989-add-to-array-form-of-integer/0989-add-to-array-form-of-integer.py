class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        total = []
        n = len(num) -1
        while k > 0 or n >= 0:
            if n >= 0:
                k+=num[n]
            total.append(k%10)
            k //= 10
            n -= 1
        total.reverse()
        return total
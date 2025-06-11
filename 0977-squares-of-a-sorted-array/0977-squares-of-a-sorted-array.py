class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for num in nums:
            num = num ** 2
            arr.append(num)
        arr.sort()
        return arr
        
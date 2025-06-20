class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        maxi = 0
        for num in nums:
            if num == 0:
                one = 0
            else:
                one += 1
            maxi = max(maxi, one)


        return maxi
        
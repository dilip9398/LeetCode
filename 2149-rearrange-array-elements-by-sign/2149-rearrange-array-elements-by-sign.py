class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        positiveIndex = 0
        negativeIndex = 1
        for n in nums:
            if n > 0:
                result[positiveIndex] = n
                positiveIndex += 2
            else:
                result[negativeIndex] = n
                negativeIndex += 2
        return result
                
        
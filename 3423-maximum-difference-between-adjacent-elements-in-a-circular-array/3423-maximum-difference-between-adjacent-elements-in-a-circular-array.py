class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        diff =  abs(nums[-1] - nums[0]) 
        for i in range(len(nums)-1):
            diff = max(diff, abs(nums[i] - nums[i+1]))
        
        return diff       
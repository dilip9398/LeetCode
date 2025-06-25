class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for num in nums:
            if num == target:
                return nums.index(num)

        return -1
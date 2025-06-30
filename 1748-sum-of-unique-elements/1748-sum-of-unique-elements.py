class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        s = set(nums)
        for item in nums:
            if nums.count(item) ==1:
                a.append(item)

        return sum(a)

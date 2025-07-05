class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hashmap = [0] * (n + 1)

        for num in nums:
            hashmap[num] += 1

        for hm in hashmap:
            if hm == 0:
                return hashmap.index(hm)
        
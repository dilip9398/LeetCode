class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indexed = [(num, i) for i, num in enumerate(nums)]
        indexed.sort(key=lambda x: -x[0])  
        topk = sorted(indexed[:k], key=lambda x: x[1])  
        return [num for num, i in topk]
        
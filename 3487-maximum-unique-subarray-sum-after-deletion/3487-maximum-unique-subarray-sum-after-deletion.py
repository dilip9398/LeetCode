class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        st = set()
        max_neg = float('-inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                st.add(nums[i])
            else:
                max_neg = max(max_neg, nums[i])
        for val in st:
            total_sum += val

        if len(st) > 0:
            return total_sum
        else:
            return max_neg
        
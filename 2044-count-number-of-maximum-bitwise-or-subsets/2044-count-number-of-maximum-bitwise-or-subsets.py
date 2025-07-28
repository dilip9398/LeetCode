class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for num in nums:
            max_or |= num  # Compute the maximum possible OR (achieved by taking all elements)

        def dfs(i, current_or):
            if i == len(nums):
                return 1 if current_or == max_or else 0
            # Include nums[i]
            include = dfs(i + 1, current_or | nums[i])
            # Exclude nums[i]
            exclude = dfs(i + 1, current_or)
            return include + exclude

        return dfs(0, 0)
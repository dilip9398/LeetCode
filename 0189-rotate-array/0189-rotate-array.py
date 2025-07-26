class Solution(object):
    def rotate(self, nums, k):
        n = len(nums) #len of the arr
        k %= n

        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        
        
from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        # count = 0
        # element = None

        # for num in nums:
        #     if count == 0:
        #         element = num
        #     count += (1 if num == element else -1)
        # return element

        # n = len(nums)
        # nums.sort()
        # return nums[n//2]

        #Using the Hashmap

        n = len(nums)
        n //= 2

        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        for key, value in hashmap.items():
            if value > n:
                return key
        return 0
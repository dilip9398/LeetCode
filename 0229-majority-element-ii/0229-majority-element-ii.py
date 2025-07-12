class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        frequency = Counter(nums)

        for k , v in frequency.items():
            if v > n//3:
                result.append(k)
        
        # result.sort()
        return result
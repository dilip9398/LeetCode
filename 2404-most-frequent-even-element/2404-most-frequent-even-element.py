from collections import Counter
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        even = [num for num in nums if num % 2 == 0]

        frequency = Counter(even)
        
       
        if not frequency:
            return -1
        

        maxi = max(frequency.values())
        
        
        mini = [num for num, cnt in frequency.items() if cnt == maxi]
        
       
        return min(mini)

        
        

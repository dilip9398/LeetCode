from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        freq = Counter(arr)
        seen = set()

        for count in freq.values():  
            if count in seen:
                return False
            seen.add(count)

        return True
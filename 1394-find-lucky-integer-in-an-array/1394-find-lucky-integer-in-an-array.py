class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)

        map = {}

        for a in arr:
            if a in map:
                map[a] += 1
            else:
                map[a] = 1

        best = -1

        for k in map.keys():
            if map[k] == k:
                best = max(best, k)

        return best
class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        right = defaultdict(list)
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))

        left = [0, 0]
        bonus = [0] * (n + 1)
        ans = 0

        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]

            ans += r - left[0]
            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]

        return ans + max(bonus)
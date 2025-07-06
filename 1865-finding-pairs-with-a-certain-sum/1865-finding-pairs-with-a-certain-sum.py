class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.f2 = collections.Counter(nums2)
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        prev = self.nums2[index]
        self.nums2[index] += val
        after = self.nums2[index]

        self.f2[prev] -= 1
        self.f2[after] += 1


    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        c = 0
        for x in self.nums1:
            c += self.f2[tot - x]
        return c
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
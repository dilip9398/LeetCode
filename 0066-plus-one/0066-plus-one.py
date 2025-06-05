class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        """
        a = [1, 0]
        if len(digits) <= 1:
            return a

        add = 1 + digits[-1]
        digits.remove(digits[-1])
        digits.append(add)

        return digits
        
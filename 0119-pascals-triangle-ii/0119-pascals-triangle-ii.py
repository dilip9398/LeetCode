class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        ans = [1]
        add = 1
        for i in range(rowIndex):
            add *= (rowIndex - i)
            add //= (i + 1)
            ans.append(add)
        return ans

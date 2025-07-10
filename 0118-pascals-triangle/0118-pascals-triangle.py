class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            result.append(self.generateRow(i))
        return result


    def generateRow(self, rowIndex):
        ans = [1]
        add = 1
        for i in range(rowIndex):
            add *= (rowIndex - i)
            add //= (i + 1)
            ans.append(add)
        return ans
        
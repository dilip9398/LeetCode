class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for i in range(n):
        #     for j in range(n//2):
        #         matrix[i][j], matrix[i][n - 1 -j] = matrix[i][n-j-1], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
        
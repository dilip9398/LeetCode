class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        divisible = []
        non_divisible = []
        for i in range(1, n+1):
            if i % m == 0:
                divisible.append(i)
            else:
                non_divisible.append(i)
        num1 = sum(divisible)
        num2 = sum(non_divisible)

        return num2 - num1
        
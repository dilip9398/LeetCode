class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        min_price = float('inf')
        profit = 0

        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)

        return profit
        
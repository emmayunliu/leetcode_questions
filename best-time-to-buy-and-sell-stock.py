# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit, minPrice = 0, float('inf')
        for i in prices:
            minPrice = min(minPrice, i)
            profit = i - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit

obj = Solution()
print obj.maxProfit([2,4,1])

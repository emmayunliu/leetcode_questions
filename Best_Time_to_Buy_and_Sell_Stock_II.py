# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            profit += max(prices[i+1] - prices[i], 0)
        return profit

obj = Solution()
print obj.maxProfit([1,2,3,4,5,6,7])
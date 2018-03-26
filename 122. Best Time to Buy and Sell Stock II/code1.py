class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        maxProfit = 0
        while i<len(prices)-1:
            if prices[i] < prices[i+1]:
                maxProfit += prices[i+1] - prices[i] 
            i += 1
        return maxProfit

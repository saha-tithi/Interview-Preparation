class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        n=len(prices)

        max_profit=0
        for i in range (1,n):
            profit=prices[i]-mini
            max_profit=max(max_profit,profit)
            mini=min(mini,prices[i])
        return max_profit
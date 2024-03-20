class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        totalProfit = 0
        l = 0

        for r in range(len(prices)):
            currentProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, currentProfit)

            if maxProfit > currentProfit:
                totalProfit += maxProfit
                maxProfit = 0
                l = r
            else:
                maxProfit = currentProfit 

            if prices[r] < prices[l]:
                l = r
            
        return maxProfit + totalProfit
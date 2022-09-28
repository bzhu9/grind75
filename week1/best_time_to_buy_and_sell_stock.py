class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentBought = prices[0]
        currentProfit = 0
        for price in prices:
            if price - currentBought > currentProfit:
                currentProfit = price - currentBought
            if price < currentBought:
                currentBought = price
        return currentProfit

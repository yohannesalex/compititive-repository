# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        effective_price = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit,prices[i] - effective_price-fee)
            effective_price = min(effective_price, prices[i] - profit)
        return profit

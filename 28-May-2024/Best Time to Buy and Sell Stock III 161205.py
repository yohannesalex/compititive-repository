# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def back(i, state, bought):
            if i == len(prices):
                return 0
            if bought > 2:
                return 0
            if state == "sell":
                buy = back(i+1, "buy", bought+1) - prices[i]
                skip = back(i+1 , "sell", bought)
                return max(buy , skip)
            if state == "buy":
                buy = back(i+1, "sell", bought) + prices[i]
                skip = back(i+1 , "buy", bought)
                return max(buy , skip)
        return back(0,"sell", 0)
            
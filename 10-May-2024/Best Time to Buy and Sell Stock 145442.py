# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = 0
        for i in range(1,len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            else:
                maxi = max(prices[i]-mini,maxi)
        return maxi

        
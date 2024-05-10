# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i , state):
            if i >= len(prices):
                return 0
            if (i , state) in memo:
                return memo[(i,state)]

            if state == 'buy':
                buy = dfs(i + 1 , 'sell') - prices[i] 
                jump = dfs(i + 1 , 'buy')
                val = max(buy , jump)
                memo[(i , state)] = val
            else:
                sell = dfs(i + 2 , 'buy') + prices[i]
                jump = dfs(i + 1 , 'sell')
                val = max(sell , jump)
                memo[(i , state)] = val
            return memo[(i , state)]
        dfs(0 , 'buy')
        return memo[(0 , 'buy')]
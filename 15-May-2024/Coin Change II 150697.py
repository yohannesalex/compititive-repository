# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        memo={}
        if amount == 0:
            return 1
        def back(total,idx):
            nonlocal res
            if total > amount:
                return 0
            if total == amount:
                
                return 1
            if (total,idx) in memo:
                return memo[(total,idx)]
            way = 0
            for i in range(idx, len(coins)):
                
                way+=back(total + coins[i], i)
            memo[(total,idx)] = way
            return memo[(total,idx)]
        return back(0, 0)
        

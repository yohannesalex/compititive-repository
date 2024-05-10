# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = set()
        dp.add(0)
        memo=set()
        for i in range(amount//min(coins)+1):
            new = set()
            for t in dp:
                for j in range(len(coins)):

                    if t + coins[j] == amount:
                        return i+1
                    if t + coins[j] < amount and t + coins[j] not in memo:
                        new.add(t + coins[j])
                        memo.add(t + coins[j])

                
            dp = new
        return -1
       
            
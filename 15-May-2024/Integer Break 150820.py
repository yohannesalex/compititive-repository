# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        memo = {}

        def dfs(n):
            if n in memo:
                return memo[n]
            if n <= 3:
                return n
            
            max_product = 0
            for i in range(1, n):
                max_product = max(max_product, i * dfs(n-i))
            
            memo[n] = max_product
            return max_product
        
        return dfs(n)

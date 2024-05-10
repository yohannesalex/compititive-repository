# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

memo= {0:0, 1:1, 2:1}
class Solution:

    def tribonacci(self, n: int) -> int:
        
        
            if n not in memo:
                memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return memo[n]
        
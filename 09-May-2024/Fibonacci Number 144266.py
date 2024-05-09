# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo={}
        def fi(n):
            if n <= 1:
                return n
           
            if n not in memo:
                memo[n] = fi(n-1) + fi(n-2)
            return memo[n]
        return fi(n)
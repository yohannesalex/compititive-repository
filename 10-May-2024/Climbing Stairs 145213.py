# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # memo ={}
        # def fib(n):
        #     prev = 1
        #     # if n<=2:
        #     #     return n
        #     # if n not in memo:
        #     #     memo[n] = fib(n-1) + fib(n-2)
        #     # return memo[n]

        # return fib(n)
        prev = 1
        prev2 = 2
        # cur = prev2
        if n == 1:
            return 1
        for i in range(3,n+1):
            cur = prev + prev2
            prev, prev2 = prev2, cur
            
        return prev2
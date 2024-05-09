# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo ={}
        def fib(i):
            if i >= n:
                return 0
            if i not in memo:
                memo[i] = max(fib(i+1),fib(i+2)+nums[i])
            return memo[i]
        return fib(0)

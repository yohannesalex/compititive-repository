# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums, target):
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for s in dp:
                next_dp[s + num] += dp[s]
                next_dp[s - num] += dp[s]
            dp = next_dp  
        return dp[target]

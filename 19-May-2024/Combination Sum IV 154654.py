# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def back(tot):
            if tot in memo:
                return memo[tot]
            if tot == target:
                return 1
            if tot > target:
                return 0
            
            res = 0
            for i in range(len(nums)):
                res += back(tot + nums[i])
            
            memo[tot] = res
            return res
        
        return back(0)

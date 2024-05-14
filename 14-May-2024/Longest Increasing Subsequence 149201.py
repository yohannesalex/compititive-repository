# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        
        def LIS(current_index):
            if current_index == len(nums):
                return 0
            if (current_index) in memo:
                return memo[current_index]
            taken = 1
            for j in range(current_index+1 , len(nums)):
                if nums[j] > nums[current_index]:
                    taken = max(taken,1 + LIS(j))

            memo[current_index] =taken
            return taken
        maxi = 0
        for i in range(len(nums)):
            maxi = max(LIS(i),maxi)
        return maxi
# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        for i in range(1,len(nums)):
            maxi = max(nums[i]- nums[i-1], maxi)
        return maxi
        
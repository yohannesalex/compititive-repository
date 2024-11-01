# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        maxi = 0
        
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                maxi = max(maxi, i - stack.pop())
        
        return maxi

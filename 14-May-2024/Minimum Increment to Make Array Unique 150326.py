# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        current = 1 + nums[0]
        for i in range(1, len(nums)):
            if current > nums[i]:
                res += current - nums[i]
                current += 1 
            else:
                current = 1 + nums[i]
        return res
        
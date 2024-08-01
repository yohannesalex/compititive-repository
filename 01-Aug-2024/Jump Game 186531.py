# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seen = set()
        if len(nums) == 1:
            return True
        if 0 not in nums:
            return True
        last = 0
        i = 0
        while i < len(nums):
            for j in range(i+1 , i+nums[i]+1):
                seen.add(j)
            i+=1
        print(seen)
        for i in range(1, len(nums)):
            if i not in seen:
                return False
        
        return True

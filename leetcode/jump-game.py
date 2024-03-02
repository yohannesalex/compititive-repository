class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        var = 0
        last_good =len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i]>=last_good:
                last_good = i
        if last_good == 0:
            return True
        return False

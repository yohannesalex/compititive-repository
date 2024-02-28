class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        total = 1
        patch = 0
        i = 0
        while total <= n:
            
            if i < len(nums) and nums[i] <= total:
                total += nums[i]
                i += 1
            else:
                total *= 2
                patch += 1
                
                
        return patch
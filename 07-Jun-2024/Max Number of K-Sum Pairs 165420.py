# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) -1
        nums.sort()
        res = 0
        while l < r:
            if nums[r] + nums[l] < k:
                l+=1
            elif nums[r] + nums[l] > k:
                r-=1
            else:
                res+=1
                l+=1
                r-=1
        return res
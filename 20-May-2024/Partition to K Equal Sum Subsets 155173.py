# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)//k
        if max(nums) > target:
            return False
        if sum(nums) % k != 0:
            return False
        
        used = [False] * len(nums)
        def back(i, k , tot):
            if  k == 0:
                return True
            if tot == target:
                return back(0,k-1,0)
            for j in range(i,len(nums)):
                if used[j] or nums[j] + tot > target:
                    continue
                
                used[j] = True
                if back(j+1,k, tot+nums[j]):
                    return True
                used[j] = False
            return False
        return back(0,k, 0)

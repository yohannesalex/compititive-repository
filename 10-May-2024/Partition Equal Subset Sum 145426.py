# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    
    def canPartition(self, nums: List[int]) -> bool:
        # @cache
        # if sum(nums) % 2 != 0:
        #     return False
        # n = sum(nums)
        # target = n//2
        # memo ={}
        # def comb(i,total):
           
        #     if total == target:
                
        #         return True
        #     elif i >= len(nums) or total > target  :
        #         return
            
        #     if comb(i+1, total+nums[i]):
        #         return True
            
        #     if comb(i+1,total):
        #         return True
        
           
            
        #     return False
        # return comb(0,0)
        if sum(nums) % 2:
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            new=set()
            for t in dp:
                if t+nums[i] == target:
                    return True
                new.add(t + nums[i])
                new.add(t)
            dp = new
        return False
        
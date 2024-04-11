# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort()
        def comb(sum,path,pos):
            if sum == target:
                res.append(path.copy())
                return 
            prev = -1
            if sum > target:
                return 
            prev = -1
            for i in range(pos,len(nums)):
                if prev == nums[i]:
                    continue
                path.append(nums[i])
                comb(sum+nums[i],path,i+1)
                path.pop()
                prev = nums[i]
        comb(0,[],0)
        return res
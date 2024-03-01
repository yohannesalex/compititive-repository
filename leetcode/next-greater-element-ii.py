class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l=0
        r=1
        res=[]
        nums.extend(nums)
        while l < len(nums)//2:
            while l < len(nums)//2 and nums[l] >= nums[r]:
                r+=1
                if r == len(nums):
                    res.append(-1)
                    l+=1
                    r=l+1
            if l < len(nums)//2 and nums[l] < nums[r]:
                res.append(nums[r])
                l+=1
                r=l+1
        return res

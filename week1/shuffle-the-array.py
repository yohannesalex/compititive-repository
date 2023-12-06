class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        l=0
        r=n
        while l <= r and r < len(nums):
            res.append(nums[l])
            res.append(nums[r])
            l+=1
            r+=1
        return res
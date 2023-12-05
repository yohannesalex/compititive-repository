class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        l=0
        r=1
        while r < len(nums):
            for i in range(nums[l]):
                res.append(nums[r])
            l+=2
            r+=2
        return res
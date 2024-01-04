class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k
        sumi=sum(nums[0:k])
        maxi=-inf
        while r < len(nums):
            maxi=max(maxi,sumi/k)
            sumi-=nums[l]
            sumi+=nums[r]
            l+=1
            r+=1
        maxi=max(maxi,sumi/k)
        return maxi


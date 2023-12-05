class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        l=1
        r=2
        k=0
        while r < len(nums):
            if nums[l] + nums[r] > nums[k]:
                return nums[l] + nums[r] + nums[k]
            l+=1
            r+=1
            k+=1
        return 0

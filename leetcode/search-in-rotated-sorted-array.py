class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            pivot =0
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    pivot=i+1
            l=0
            r=len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[(mid+pivot)%len(nums)] == target:
                    return (mid+pivot)%len(nums)
                elif nums[(mid+pivot)%len(nums)] > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
            
            
            
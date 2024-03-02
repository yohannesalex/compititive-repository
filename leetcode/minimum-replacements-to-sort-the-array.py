class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0
        last = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            
            if nums[i] > last:
                res = ((nums[i])//last)
                
                if nums[i] % last:
                    res += 1
                op += res-1
                last = nums[i]//res
            else:
                last = nums[i]
        return op

        
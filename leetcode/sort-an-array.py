class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<= 1:
                return nums
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        
        
        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)
        
        return merge(left_half, right_half)
    def merge(left,right):
        new=[]
        l = 0
        r =0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                new.append(left[l])
                l+=1
            else:
                new.append(right[r])
                r+=1
        while l < len(left):
            new.append(left[l])
            l += 1
    
        while r < len(right):
            new.append(right[r])
            r += 1
    
    

        return new

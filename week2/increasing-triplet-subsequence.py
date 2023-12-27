class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len (nums) < 3:
            return False
        else:
            i=2**31
            j=2**31
            for l in nums:
                if l <= i:
                    i=l
                elif  l <= j:
                    j=l 
                else:
                    return True
            return False 

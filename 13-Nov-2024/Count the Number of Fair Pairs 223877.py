# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  # Step 1: Sort the array for efficient searching
        n = len(nums)
        ans = 0
        
        for i in range(n):
            # Calculate the minimum and maximum values that can pair with nums[i]
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            
            # Step 2: Use binary search to find the range within bounds
            # Start from index i+1 to ensure i < j
            left_index = bisect_left(nums, min_val, i + 1)
            right_index = bisect_right(nums, max_val, i + 1)
            
            # Count valid pairs for nums[i]
            ans += (right_index - left_index)
        
        return ans

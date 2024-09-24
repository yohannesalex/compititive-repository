# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  
        left = 0  
        total_sum = 0  
        max_freq = 0  

        for right in range(len(nums)):
            total_sum += nums[right] 

            while (right - left + 1) * nums[right] > total_sum + k:
                total_sum -= nums[left]  
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        l=0
        r=0
        max_score=0
        curr_score = 0
        elements = set()
        while r < len(nums):
            while nums[r] in elements:
                elements.remove(nums[l])
                curr_score -= nums[l]
                l+= 1

            curr_score += nums[r]
            elements.add(nums[r])
            max_score = max(curr_score, max_score)
            r+= 1

        return max_score
# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]*=-1
        heapify(nums)
        for i in range(k):
            ans = heapq.heappop(nums)
        return -1*ans

        # return heapq.nlargest(k, nums).pop()
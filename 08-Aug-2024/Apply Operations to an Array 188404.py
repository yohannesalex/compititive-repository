# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        cur = []
        zeros = 0
        for i in nums:
            if i != 0:
                cur.append(i)
            else:
                zeros+=1
        for i in range(zeros):
            cur.append(0)
        return cur

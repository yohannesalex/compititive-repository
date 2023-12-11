class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for idx,e in enumerate(nums):
            val=target-e
            if val in prev:
                return [idx,prev[val]]
            else:
                prev[e]=idx
        
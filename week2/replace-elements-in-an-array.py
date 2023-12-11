class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_dict = {}  # A dictionary to store the indices of elements in nums
        for i in range(len(nums)):
            index_dict[nums[i]] = i

        for k, v in operations:
            if k in index_dict:
                index = index_dict[k]
                nums[index] = v
                index_dict[v] = index
                del index_dict[k]

        return nums

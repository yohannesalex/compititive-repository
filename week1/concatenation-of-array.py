class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        clone=[]

        for i in nums:
            clone.append(i)
        for i in nums:
            clone.append(i)
        return clone
        
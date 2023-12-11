
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i in count:
            if count.get(i) > 1:
                return True
        return False
        
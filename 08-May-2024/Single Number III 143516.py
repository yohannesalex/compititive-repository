# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cur = 0
        for i in nums:
            cur = cur^i
        mask = cur & -cur
        
        set1 = 0
        set2 = 0
        for num in nums:
            if num&mask:
                set1^=num
            else:
                set2^=num
        return [set1,set2]

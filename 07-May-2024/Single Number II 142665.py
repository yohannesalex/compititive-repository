# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count_bits = 0
            for num in nums:
                if num & (1 << i):
                    count_bits+=1
            
            ans |= (count_bits % 3) << i
        if ans >= 1 << 31:
            ans -= 1 << 32
        return int(ans)
            
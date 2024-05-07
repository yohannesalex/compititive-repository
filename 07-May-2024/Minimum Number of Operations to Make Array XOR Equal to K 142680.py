# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(32):
            count = 0
            check = k & (1 << i)
            for num in nums:
                if num & 1 << i:
                    count+=1
            if count% 2 == 0:
                if check:
                    ans+=1
            else:
                if not check:
                    ans +=1
        return ans

            
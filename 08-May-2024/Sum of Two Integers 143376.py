# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        rem = 0
        for i in range(32):
            num1, num2= a&(1<<i), b&(1<<i)
            if num1:
                rem +=1
            if num2:
                rem +=1
            ans |= (rem%2 << i)
            rem//=2
        if ans >= (1 << 31):
            ans -= (1 << 32)
        return ans

        
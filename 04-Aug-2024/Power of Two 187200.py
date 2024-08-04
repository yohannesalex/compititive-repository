# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        k = bin(n)
        
        return True if  n >0 and  k.count("1") == 1 else  False
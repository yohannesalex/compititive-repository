# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)
        print(s)
        po = 32 - len(s)
        res = 0
        for i in s:
            if i == "1":
                res += 2**po
            po+=1
        return res

        
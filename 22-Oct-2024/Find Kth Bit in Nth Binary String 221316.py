# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev(s):
            cur = ''
            for i in range(len(s)-1,-1,-1):
                if s[i] == '0':
                    cur+='1'
                else:
                    cur+='0'

            return cur
        s= '0'
        for i in range(1,n):
            s = s+'1'+ rev(s)
        return s[k-1]

# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        k = bin(num)
        st = str(k)
        stri = ""
        for i in range(len(st)):
            if st[i] == "1":
                st = st[i:]
                break
        ans = ""
        
        for i in st:
            if i == "0":
                ans+="1"
            else:
                ans+="0"
        res=0
        j =0
        
        for i in range(len(ans)-1,-1,-1):
            res+=int(ans[i])*(2**j)
            j+=1
        return res
        
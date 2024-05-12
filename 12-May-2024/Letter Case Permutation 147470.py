# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = list(s)
        result = []

        def backtrack(start):
            if start == len(s):     
                result.append(''.join(s))
                return

            for i in range(start, len(s)):
                if s[i].isalpha():
                    s[i] = chr(ord(s[i]) ^ 32)  
                    backtrack(i + 1)
                    s[i] = chr(ord(s[i]) ^ 32) 
            backtrack(len(s)) 
        backtrack(0)

        return result
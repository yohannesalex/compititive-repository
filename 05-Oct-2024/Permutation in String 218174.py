# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        comp = Counter(s1)
        width = len(s1)
        l = 0
        r = width
        while r <= len(s2):
            cur = Counter(s2[l:r])
            if cur == comp:
                return True
            l+=1
            r+=1
        return False

# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def check(l , r , s):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        path = []
        def back(i):
            if i == len(s):
                res.append(path.copy())
                
            for j in range(i,len(s)):
                if check(i,j,s):
                    path.append(s[i:j+1])
                    back(j+1)
                    path.pop()
            
        back(0)
        return res
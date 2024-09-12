# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        ans = 0
        for word in words:
            flag = True
            for j in word:
                if j not in allow:
                    flag = False
            if flag:
                ans+=1

        return ans
# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for char in t:
            if idx == len(s):
                return True
            if char == s[idx]:
                idx += 1
        return idx == len(s)

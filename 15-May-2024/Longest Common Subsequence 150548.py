# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo={}
        def back(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + back(i+1, j+1)
            else:
                memo[(i,j)] = max(back(i+1,j),back(i,j+1))
            return memo[(i,j)]
        return back(0,0)
       
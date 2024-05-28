# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)
        memo = [0] * (n + 1)
        memo[n] = 0

        def valid(start, end):
            temp = s[start:end+1]
            return temp == temp[::-1]

        if valid(0, n-1):
            return 0

        for i in range(n-1, -1, -1):

            min_cuts = float('inf')
            
            for j in range(i, n):
                if valid(i, j):
                    cut = 1 + memo[j+1]
                    min_cuts = min(min_cuts, cut)

            memo[i] = min_cuts

        return memo[0] -1
# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * N
        for i in range(N-1,-1,-1):
            dp[i]=questions[i][0]
            jump = i+questions[i][1]+1
            if jump < N:
                dp[i]+=dp[jump]
            if i < N-1:
                dp[i] = max(dp[i], dp[i+1])
        return max(dp)
# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        dp= [[-float('inf')]*n for _ in range(m)] 

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if (i,j)==(m-1, n-1):
                    dp[-1][-1] = max(1, -dungeon[-1][-1]+1)
                elif i==m-1:
                    dp[i][j] = max(1, dp[i][j+1]-dungeon[i][j])
                elif j==n-1:
                    dp[i][j] = max(1, dp[i+1][j]-dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])


        return dp[0][0]



                


            
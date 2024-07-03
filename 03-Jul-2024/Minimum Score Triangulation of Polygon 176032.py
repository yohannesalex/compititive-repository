# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(v1, v2) :
            if v2 - v1 <= 1:
                return 0
            ans = inf
            for pos in range(v1 + 1, v2):
                ans = min(ans, dp(v1, pos) + dp(pos, v2) + values[v1] * values[v2] * values[pos])
            return ans

        return dp(0, len(values) - 1)
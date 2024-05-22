# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        stone_pos = {stone: idx for idx, stone in enumerate(stones)}
        
        @cache
        def back(i, k):
            if i == n - 1:
                return True
            for jump in (k - 1, k, k + 1):
                if jump <= 0:
                    continue
                next_pos= stones[i] + jump
                if next_pos in stone_pos:
                    next_index = stone_pos[next_pos]
                    if back(next_index, jump):
                        return True
            return False
        
        return back(0, 0)

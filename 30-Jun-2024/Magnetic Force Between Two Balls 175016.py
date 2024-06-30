# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def is_possible(step):
            next_pos, cnt = 0, 0
            for pos in position:
                if pos >= next_pos:
                    next_pos = pos + step
                    cnt += 1
                    if cnt == m:
                        return True
            return False

        position.sort()
        ans, left, right = 0, 1, (position[-1]-position[0])//(m-1)
        while left <= right:
            middle = (left+right)//2
            if is_possible(middle):
                ans = middle
                left = middle+1
            else:
                right = middle-1 
        return ans
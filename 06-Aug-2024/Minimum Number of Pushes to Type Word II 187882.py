# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        res = i = 0
        for n in sorted(Counter(word).values(), reverse=True):
            res += n * (i // 8 + 1)
            i += 1
        return res
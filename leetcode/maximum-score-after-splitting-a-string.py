class Solution:
    def maxScore(self, s: str) -> int:
        ans = -999
        l0 = 0
        r1 = 0
        t0 = s.count('0')
        t1 = s.count('1')
        for i in range(len(s)-1):
            if s[i] == '0':
                t0 -= 1
                l0 += 1
                if l0 + t1 > ans:
                    ans = l0 + t1
            else:
                t1 -= 1
                if l0 + t1 > ans:
                    ans = l0 + t1
        return ans
# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_read = 0
        s_read = 0
        answer = 0
        while g_read < len(g) and s_read < len(s):
            if g[g_read] <= s[s_read]:
                answer+=1
                g_read+=1
                s_read+=1
            else:
                s_read+=1
        return answer

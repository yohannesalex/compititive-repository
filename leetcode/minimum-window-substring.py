class Solution(object):
    def minWindow(self, s, t):
        
        if len(t) > len(s):
            return ""

        res = ""
        m = len(s) + 1
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for i in t:
            map1[i] += 1
        
        n = len(map1)
        l = cnt = 0

        for r in range(len(s)):
            if s[r] in map1:
                map2[s[r]] += 1

                if map2[s[r]] == map1[s[r]]:
                    cnt += 1

                    while cnt == n:
                        if r-l+1 < m:
                            m = r-l+1
                            res = s[l:r+1]

                        if s[l] in map2:
                            map2[s[l]] -= 1

                            if map2[s[l]] < map1[s[l]]:
                                cnt -= 1
                        l += 1
        return res 
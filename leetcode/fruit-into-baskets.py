class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        mapp = {}
        i, j, ans = 0, 0, 0

        while j < n:
            mapp.setdefault(fruits[j], 0)
            mapp[fruits[j]] += 1
            if len(mapp) < 3: 
                ans = max(ans, j - i + 1)
            else:
                mapp[fruits[i]] -= 1

                
                if mapp[fruits[i]] == 0:
                    mapp.pop(fruits[i])
                i += 1


            j += 1
        return ans

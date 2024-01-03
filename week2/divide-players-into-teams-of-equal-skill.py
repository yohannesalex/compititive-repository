class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res=0
        l=0
        r=len(skill)-1
        while l+1 < r-1:
            if skill[l] + skill[r] != skill[l+1] + skill[r-1] :
                return -1
            res+=(skill[l] * skill[r])
            l+=1
            r-=1
        res+=(skill[l] * skill[r])
        return res
        
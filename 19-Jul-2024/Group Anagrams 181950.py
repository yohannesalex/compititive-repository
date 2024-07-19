# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        ans = []
        for st in strs :
            cur = list(st)
            cur.sort()
            c = "".join(cur)
            count[c].append(st)
        for key , val in count.items():
            ans.append(val)
        return ans

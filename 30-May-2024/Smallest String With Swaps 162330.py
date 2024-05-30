# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = len(s)
        parents = {i:i for i in range(len(s))}
        rank = defaultdict(int)

        def find(x):
        # Write your code here
            if x == parents[x]:
                return x
            par = find(parents[x])
            parents[x] = par
            return par
        
        def union(x, y):
        # Write your code here
            x = find(x)
            y = find(y)

            if x != y:
                if rank[x] > rank[y]:
                    parents[y] = x
                elif rank[x] < rank[y]:
                    parents[x] = y
                else:
                    parents[x] = y
                    rank[y] += 1
                # return True
        
        for u , v in pairs:
            union(u , v)


        swapped = defaultdict(list)
        for key in parents:
            x = find(key)
            swapped[x].append(key)
        
        for key in swapped:
            swapped[key].sort(key = lambda x : s[x], reverse = True)
        
        res = []
        for char in range(len(s)):
            x = find(char)
            ans = swapped[x][-1]
            swapped[x].pop()
            res.append(s[ans])
        return "".join(res)










        
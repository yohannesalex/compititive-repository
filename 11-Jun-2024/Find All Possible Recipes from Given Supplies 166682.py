# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rMap = {}
        indegreeM = {}
        res = []
        not_possible = set()

        for i in range(len(recipes)):
            for t in ingredients[i]:
                if recipes[i] in indegreeM:
                    indegreeM[recipes[i]] += 1 
                else:
                    indegreeM[recipes[i]] =1

                if (t not in supplies and t not in recipes) or t in not_possible:
                    not_possible.add(recipes[i])
                    continue

                ingrList = rMap.setdefault(t, [])
                ingrList.append(recipes[i])
                igrInList = indegreeM.setdefault(t, 0)

                
        q = deque([])
        for key, value in indegreeM.items():
            if value == 0:
                q.append(key)
        # print(q)

        
        
        while len(q) != 0:
            t = q.popleft()

            if t in rMap:
                for nei in rMap[t]:
                    indegreeM[nei] -=1
                    if indegreeM[nei] == 0:
                        res.append( nei )
                        q.append(nei)

        return res


        

        



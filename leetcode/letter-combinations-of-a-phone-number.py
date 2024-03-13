class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = {"2":"abc", "3":"def", "4":"ghi" , "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res=[]
        cur=[]
        def back(i,cur):
            if len(cur) == len(digits):
                res.append("".join(cur.copy()))
                return
            for char in store[digits[i]]:
                cur.append(char)
                back(i+1,cur)
                cur.pop()
        if digits:        
            back(0,[])
        else:
            return res
        return res


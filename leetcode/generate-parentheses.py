class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        
        def generate(oc,cc,cur):
            if oc == cc == n:
                res.append("".join(cur))
                return
            
            if oc < n:
                cur.append("(")
                generate(oc+1, cc ,cur)
                cur.pop()
            if cc < oc:
                cur.append(")")
                generate(oc,cc+1,cur)
                cur.pop()
        generate(0,0,[])
        return res
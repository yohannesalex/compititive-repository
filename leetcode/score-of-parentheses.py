class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        val=0
        total=0
        stack=[]
        for i in s:
            if i== "(":
                stack.append(0)
            else:
                mul=stack.pop()
                if  mul == 0:
                    val=1
                else:
                    val=mul*2
                
                if not stack:
                    total+=val
                else:
                    stack[-1]+=val
        return total


                    
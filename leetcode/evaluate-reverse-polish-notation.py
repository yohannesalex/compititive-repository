class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
       
        op="+-*/"
        for i in tokens:
            if i  not in op:
                stack.append(int(i))
            elif i  in op:
                if i=="+":
                    k=stack[-2] + stack[-1]
                elif i=="-":
                    k=stack[-2] - stack[-1]
                elif i=="*":
                    k=stack[-2] * stack[-1]
                elif i=="/":
                    k=stack[-2] // stack[-1]
                    if k < 0 and stack[-2] // stack[-1]!=stack[-2] / stack[-1] :
                        k=k+1
                stack.pop()
                stack.pop()
                stack.append(k)
        return stack[0]


        
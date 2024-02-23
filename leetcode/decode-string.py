class Solution:
    def decodeString(self, s: str) -> str:
        # stack=[]
        # nums="0123456789"
        # for i in s:
        #     if i =="]":
        #         k=""
        #         while stack and stack[-1] != "[":
        #             k=stack.pop()+k
        #         stack.pop()
        #         num=""
        #         while stack and stack[-1] in nums:
        #             num = stack.pop() + num
        #         stack.append(int(num)*k) 
        #     else:
        #         stack.append(i) 
            
        # return "".join(stack)
        if s =="":
            return ""
        pre=[]
        l=0

        while l < len(s) and not s[l].isdigit():
            pre.append(s[l])
            l+=1
        k=""
        while l < len(s) and s[l].isdigit():
            k+=s[l]
            l+=1

        k=int(k if k else 1)
        cur=[]
        open=1
        l+=1
        while l < len(s):
            if s[l] == '[':
                open+=1
            elif s[l] == "]":
                open-=1
            if open ==0:
                break
            cur.append(s[l])
            l+=1
        
        return "".join(pre) + k*self.decodeString("".join(cur)) + self.decodeString(s[l+1:])

        

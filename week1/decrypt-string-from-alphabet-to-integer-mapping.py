class Solution:
    def freqAlphabets(self, s: str) -> str:
        letter="abcdefghijklmnopqrstuvwxyz"
        stack=[]
        ans=[]
        for i in s:
            if i!="#":
                stack.append(i)
                ans.append(letter[int(i)-1])
            else:
                k=""
                k=stack.pop()+k
                k=stack.pop()+k
                ans.pop()
                ans.pop()
                ans.append(letter[int(k)-1])
        return "".join(ans)

                
                
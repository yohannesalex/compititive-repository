class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        st=[]
        if len(palindrome) ==1:
            return ""
        else:
                
            for i in range(len(palindrome)):
                st.append(palindrome[i])
            
            for i in range(len(st)):
                if len(st)%2 == 1 and i == len(st)//2:
                    continue
                elif st[i] != "a":
                    st[i] = "a"
                    break
                
            else:
                st[-1] = "b"

            
        return "".join(st)


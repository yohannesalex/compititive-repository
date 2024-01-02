class Solution:
    def isPalindrome(self, s: str) -> bool:
        d="abcdefghijklmnopqrstuvwxyz"
        f="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        a=""
        c=""
        for i in range(len(s)):
            if s[i]  in d or s[i] in f  :
                a+=s[i].lower()
            else:
                pass
     
        for i in range(-1,-len(a)-1,-1):
            c+=a[i]
        
        if a==c:
            return True
        else:
            return False